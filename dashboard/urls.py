from django.urls import path
from .views import login_api
from .views import logout_api
from .views import protected_view

urlpatterns = [
    path('api/logout/', logout_api, name='logout_api'),
    path('api/login/', login_api, name='login_api'),
    path('api/protected_view/', protected_view, name='protected_view'),
]