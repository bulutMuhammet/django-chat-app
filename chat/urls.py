# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('a/<str:room_name>/', views.room, name='room'),
    path('test/',views.testin,name="test")
]