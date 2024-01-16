from django.urls import path
from . import views

urlpatterns = [
    path('message/', views.MessageAPIView.as_view(), name='message')
]
