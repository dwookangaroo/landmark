from django.contrib import admin
from django.urls import path
from . import views

app_name = 'landmarkApp'

urlpatterns = [
    path('hotel/', views.hotel_recommendation, name='hotel'),
    path('restaurant/', views.restaurant_recommendation, name='restaurant'),
    path('info/', views.info, name='info')
]