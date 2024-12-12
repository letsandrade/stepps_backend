from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from dashboard.models import IndicatorModel, ChartModel

@csrf_exempt
def login_api(request):
    """
    API endpoint for user login.
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'}, status=200)
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def logout_api(request):
    """
    API endpoint for user logout.
    """
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': 'Logout successful'}, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@login_required
def indicators_api(request):
    """
    API endpoint for indicators.
    """
    indicators = IndicatorModel.objects.all()
    data = [{"name": ind.name, "value": ind.value} for ind in indicators]
    return JsonResponse(data, safe=False)

@login_required
def chart_data_api(request):
    """
    API endpoint for chart data.
    """
    chart = ChartModel.objects.get(name="number of alerts per hour")
    data_points = chart.data_points.all()
    data = {
        "name": chart.name,
        "data": [{"label": dp.label, "value": dp.value} for dp in data_points],
    }
    return JsonResponse(data)
