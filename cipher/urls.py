from django.urls import path, re_path
from . import views, functions

urlpatterns = [
    path('', views.index),
    path('page1', views.page1),
    path('page2', views.page2),
    path('page3', views.page3),
    path('page4', views.page4),
    path('page5', views.page5),
    path('page6', views.page6),
    path('page7', views.page7),
    path('page8', views.page8),
    path('action_a', functions.action_a),
    path('action_b', functions.action_b),
    path('action_c', functions.action_c),
    path('action_d', functions.action_d),
    path('action_e', functions.action_e),
    path('action_f', functions.action_f),
    path('action_g', functions.action_g),
    path('action_h', functions.action_h),
]