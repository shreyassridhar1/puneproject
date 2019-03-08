from datetime import datetime

from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django.http import HttpResponse
from weather_metrics.models import WeatherData
from rest_framework.response import Response



class MetricsListViewSet(viewsets.GenericViewSet):

    def list(self, request):
        parameters = request.query_params
        metrics = parameters.get('metrics', None)
        location = parameters.get('location', None)
        start_date = parameters.get('start_date', None)
        start_date = datetime.strptime(start_date, '%Y-%d')
        end_date = parameters.get('end_date', None)
        end_date = datetime.strptime(end_date, '%Y-%d')

        main_queryset = WeatherData.objects.all()
        if metrics:
            main_queryset = main_queryset.filter(metrics=metrics)
        if location:
            main_queryset = main_queryset.filter(location=location)
        if start_date:
            main_queryset = main_queryset.filter(date__gte=start_date)
        if end_date:
            main_queryset = main_queryset.filter(date__lte=end_date)
        res = []
        for data in main_queryset:
            res1 = []
            location = data.location
            metrics = data.metrics
            content = str(data.date) + ': ' + str(data.content)
            res1.append(content)
            res.append({'location': location, 'content': res1, 'metrics': metrics})

        return Response(res)