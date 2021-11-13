from django.contrib import admin
from .models import Facility, Manufacturer, Vaccine, Batch, Vaccination, NextVaccination


# Register your models here.
admin.site.register(Facility)
admin.site.register(Manufacturer)
admin.site.register(Vaccine)
admin.site.register(Batch)
admin.site.register(Vaccination)
admin.site.register(NextVaccination)

