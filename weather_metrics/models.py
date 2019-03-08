# from django.contrib.postgres.fields import JSONField
from django.db import models
from jsonfield import JSONField
# Create your models here.




class WeatherData(models.Model):
    MAX_TEMP = "Tmax"
    MIN_TEMP = "Tmin"
    RAINFALL = "Rainfall"
    metric_choice = [(MAX_TEMP, 'Maximum Temperature'), (MIN_TEMP, 'Minimum Temperature'), (RAINFALL, 'Rainfall')]
    metrics = models.CharField(choices=metric_choice, default='Tmax', null=True, blank=True, max_length=1000)
    location = models.CharField(max_length=500, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    content = JSONField(blank=True, null=True)


    def __str__(self):
        return (self.location + '_' + self.metrics)

    class Meta:
        db_table = 'weather_data'