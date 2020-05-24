from django.urls import path
from . import views, functions

urlpatterns = [
    path('', views.top),
    path('decode_a', functions.decode_a),
    path('decode_b', functions.decode_b),
]