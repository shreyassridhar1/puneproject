import requests
from django.core.management.base import BaseCommand
from weather_metrics.models import WeatherData
import urllib.request, json
from dateutil import parser
from datetime import datetime



class Command(BaseCommand):
    help = 'Create groups and setup permissions for teams'

    def handle(self, *args, **options):
        WeatherData.objects.all().delete()
        metrics_list = ['Tmax', 'Tmin', 'Rainfall']
        location_list = ['UK', 'England', 'Scotland', 'Wales']
        all_objects = []
        for metric in metrics_list:
            for location in location_list:
                json_data = requests.get("https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/{}-{}.json".format(metric, location), verify=False)
                content = json_data.content
                dic = json.loads(content.decode('utf-8'))
                new_list = list()

                for item in dic:
                    value = item['value']
                    month = item['month']
                    year = item['year']
                    date = str(item['year']) + '-' + str(item['month'])
                    dt = parser.parse(date)
                    datetime_object = datetime.strptime(date, '%Y-%d')

                    new_list.append({"value": value, "month": month, "year": year, "date": datetime_object})
                for object in new_list:
                    value = object.get('value')
                    date = object.get('date')


                    weather_object = WeatherData(metrics=metric, location=location, content=value, date=date)
                    all_objects.append(weather_object)

        WeatherData.objects.bulk_create(all_objects)


