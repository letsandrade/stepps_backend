from django.contrib import admin
from .models import ChartModel, DataPointModel, IndicatorModel

@admin.register(ChartModel)
class ChartModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(DataPointModel)
class DataPointModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'chart', 'label', 'value')

@admin.register(IndicatorModel)
class IndicatorModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
