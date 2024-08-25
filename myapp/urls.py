from django.urls import path
from .views import bfhl_view

urlpatterns = [
    path('bfhl/', bfhl_view, name='bfhl'),
    path('bfhl', bfhl_view, name='bfhl_without_slash'),
]
