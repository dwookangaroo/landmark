from django.contrib import admin
from django.urls import path
from . import views

app_name = 'landmarkApp'

urlpatterns = [
    path('', views.hotel_recommendation, name='hotel')
]