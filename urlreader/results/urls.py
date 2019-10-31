from django.urls import path
from . import views

urlpatterns = [
    path('', views.results, name='index')
]