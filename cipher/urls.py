from django.urls import path
from . import views, functions

urlpatterns = [
    path('', views.top),
    path('decode_alice', functions.decode_alice)
]