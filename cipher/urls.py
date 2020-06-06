from django.urls import path, re_path
from . import views, functions

urlpatterns = [
    path('', views.index),
    path('link.html', views.link),
    path('page<int:page_number>', views.pageView),
    path('action_<int:action_number>', functions.action),
]
