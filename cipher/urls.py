from django.urls import path, re_path
from . import views, functions

urlpatterns = [
    path('', views.index),
    path('page1.html', views.page1),
    path('page2.html', views.page2),
    path('page3.html', views.page3),
    path('decode_a', functions.decode_a),
    path('decode_b', functions.decode_b),
    path('decode_c', functions.decode_c),
    path('decode_d', functions.decode_d),
    path('decode_e', functions.decode_e),
]