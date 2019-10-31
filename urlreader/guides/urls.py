from django.urls import path
from . import views

urlpatterns = [
    path('', views.guides, name='index')
]