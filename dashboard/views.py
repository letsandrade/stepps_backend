from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from dashboard.models import IndicatorModel, ChartModel
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView

@csrf_exempt
def login_api(request):
    """
    API endpoint for user login.
    """
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
        # Generate JWT token using the simple JWT package
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        # Get user info (email, name, profile picture)
        user_info = {
            'username': user.username,
            'email': user.email,
            'name': user.first_name,  # Or use user.get_full_name() if you prefer
            'profile_picture': user.userprofile.profile_picture.url if hasattr(user, 'userprofile') else None,
            'access_token': access_token,
        }

        return Response(user_info, status=status.HTTP_200_OK)
    
    return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

@csrf_exempt
def logout_api(request):
    """
    API endpoint for user logout.
    """
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': 'Logout successful'}, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def indicators_api(request):
    indicators = IndicatorModel.objects.all()
    data = [{"name": ind.name, "value": ind.value} for ind in indicators]
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def chart_data_api(request):
    chart = ChartModel.objects.get(name="number of alerts per hour")
    data_points = chart.data_points.all()
    data = {
        "name": chart.name,
        "data": [{"label": dp.label, "value": dp.value} for dp in data_points],
    }
    return Response(data)
