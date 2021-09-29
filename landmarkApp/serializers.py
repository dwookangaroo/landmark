from rest_framework import serializers
from .models import Landmarks, Hotels, Restaurants


class LandmarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landmarks
        fields = ['name', 'desc', 'address', 'lat', 'lng']


class HotelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotels
        fields = ['name', 'address', 'lat', 'lng']


class RestaurantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurants
        fields = ['name', 'address', 'lat', 'lng']