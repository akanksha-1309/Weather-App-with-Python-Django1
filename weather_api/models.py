from django.db import models

class CityWeather(models.Model):
    city_name = models.CharField(max_length=100)
    temperature = models.FloatField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.city_name
