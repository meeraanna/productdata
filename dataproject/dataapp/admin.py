from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import DataModel

# Register your models here.
class DataAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['API_WELL_NUMBER','OIL','GAS','BRINE']

admin.site.register(DataModel,DataAdmin)