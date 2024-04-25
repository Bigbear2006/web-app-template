from django.urls import path
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

from . import views

urlpatterns = [
    path('get-token/', token_obtain_pair, name='get-token'),
    path('refesh-token/', token_refresh, name='refresh-token'),
    path('register/', views.RegisterUserAPIView.as_view(), name='register'),
    path('user/', views.UserRetrieveUpdateAPIView.as_view(), name='user'),
]
