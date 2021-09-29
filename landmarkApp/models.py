from django.db import models


class Landmarks(models.Model):
    name = models.CharField(max_length=255)
    #desc = models.TextField()
    #address = models.CharField(max_length=10, default='')
    lat = models.FloatField()
    lng = models.FloatField()


class Hotels(models.Model):
    rank = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    lat = models.FloatField()
    lng = models.FloatField()


class Restaurants(models.Model):
    name = models.CharField(max_length=255)
    represent = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    lat = models.FloatField()
    lng = models.FloatField()

class Transportation(models.Model):
    name = models.CharField(max_length=10)
    dwdw = models.CharField(max_length=10)

# Create your models here.
