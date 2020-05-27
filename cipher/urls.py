from django.urls import path, re_path
from . import views, functions

urlpatterns = [
    path('', views.index),
    path('page1.html', views.page1),
    path('page2.html', views.page2),
    path('page3.html', views.page3),
    path('page4.html', views.page4),
    path('page5.html', views.page5),
    path('page6.html', views.page6),
    path('action_a', functions.action_a),
    path('action_b', functions.action_b),
    path('action_c', functions.action_c),
    path('action_d', functions.action_d),
    path('action_e', functions.action_e),
    path('action_f', functions.action_f),
]