from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from . import views

from weather_metrics.views import MetricsListViewSet

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    path('list', MetricsListViewSet.as_view({'get':'list'}), name='metrics-list'),
]