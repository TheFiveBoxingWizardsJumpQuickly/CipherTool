from django.urls import path

from . import views

urlpatterns = [
    path('1200px-US_ANSI_keyboard_character_layout_JIS_comparison.svg.png', views.index, name='index'),
]