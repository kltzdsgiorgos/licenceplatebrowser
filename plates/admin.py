from django.contrib import admin
from plates.models import Plate


class PlateAdmin(admin.ModelAdmin):
    pass


admin.site.register(Plate, PlateAdmin)
