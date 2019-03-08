from django.contrib import admin




from .models import WeatherData
# from .models import Location

# Register your models here.

admin.site.register(WeatherData)
# admin.site.register(Location)




class WeatherDataAdmin(admin.ModelAdmin):
    model = WeatherData
    list_display = ['location', 'metrics']