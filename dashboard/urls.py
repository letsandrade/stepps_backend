from django.urls import path
from .views import login_api, logout_api, indicators_api, chart_data_api
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/login/', login_api, name='login_api'),
    path('api/logout/', logout_api, name='logout_api'),
    path('api/indicators/', indicators_api, name='indicators_api'),
    path('api/chart-data/', chart_data_api, name='chart_data_api'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]