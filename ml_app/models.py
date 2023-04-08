from django.db import models

class Location(models.Model):
    OCEAN_PROXIMITY_CHOICES = [
        ('ocean_proximity_<1H OCEAN', '<1H OCEAN'),
        ('ocean_proximity_INLAND', 'INLAND'),
        ('ocean_proximity_ISLAND', 'ISLAND'),
        ('ocean_proximity_NEAR BAY', 'NEAR BAY'),
        ('ocean_proximity_NEAR OCEAN', 'NEAR OCEAN'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=255,
        choices=OCEAN_PROXIMITY_CHOICES,
    )

class Prediction(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    housing_median_age = models.FloatField()
    total_rooms = models.FloatField()
    total_bedrooms = models.FloatField()
    population = models.FloatField()
    households = models.FloatField()
    median_income = models.FloatField()
    ocean_proximity = models.ForeignKey(Location, on_delete=models.CASCADE)
    price = models.FloatField()