from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/top', views.index, name='top'),
    path('/results', views.results, name='results'),
    path('/guides', views.guides, name='guides')
]