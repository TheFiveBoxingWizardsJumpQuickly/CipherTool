from django.urls import path
from . import views, functions

urlpatterns = [
    path('', views.top),
    path('sample', functions.sample)
]