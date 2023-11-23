from django.urls import path
from .views import index, auth

urlpatterns = [
    path('', index, name='index'),
    path('auth', auth, name='auth'),
]