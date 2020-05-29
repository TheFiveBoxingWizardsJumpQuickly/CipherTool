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
    path('page9', views.page9),
    path('action_1', functions.action_1),
    path('action_2', functions.action_2),
    path('action_3', functions.action_3),
    path('action_4', functions.action_4),
    path('action_5', functions.action_5),
    path('action_6', functions.action_6),
    path('action_7', functions.action_7),
    path('action_8', functions.action_8),
    path('action_9', functions.action_9),
]