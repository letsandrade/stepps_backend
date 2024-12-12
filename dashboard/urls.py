from django.urls import path
from .views import login_api, logout_api, indicators_api, chart_data_api

urlpatterns = [
    path('api/login/', login_api, name='login_api'),
    path('api/logout/', logout_api, name='logout_api'),
    path('api/indicators/', indicators_api, name='indicators_api'),
    path('api/chart-data/', chart_data_api, name='chart_data_api'),
]