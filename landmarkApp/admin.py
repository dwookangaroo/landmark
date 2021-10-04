from django.contrib import admin
from .models import Landmarks, Hotels, Restaurants, Transportation
# Register your models here.
admin.site.register(Landmarks)
admin.site.register(Hotels)
admin.site.register(Restaurants)
admin.site.register(Transportation)