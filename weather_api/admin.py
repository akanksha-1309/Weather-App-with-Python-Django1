from django.contrib import admin
from .models import CityWeather

@admin.register(CityWeather)
class CityWeatherAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'temperature', 'description')  # Display fields in admin dashboard
    search_fields = ('city_name',)  # Enable search by city name
    list_filter = ('description',)  # Enable filtering by weather description
    ordering = ('city_name',)  # Sort by city name by default
