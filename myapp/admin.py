from django.contrib import admin
from . import models


class StackedInline(admin.StackedInline):
    model = models.StackedModel


class TabularInline(admin.TabularInline):
    model = models.TabularModel


@admin.register(models.ManyInstancesModel)
class ManyInstancesModelAdmin(admin.ModelAdmin):
    inlines = [StackedInline, TabularInline]


@admin.register(models.ForeignKeyModel)
class ForeignKeyModelAdmin(admin.ModelAdmin):
    raw_id_fields = ['parent']
    list_display = ['text', 'text2']


@admin.register(models.UnchangeableModel)
class UnchangeableModelAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False
