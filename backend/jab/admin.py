from django.contrib import admin
from .models import Facility, Manufacturer, Vaccine, Vaccination


# Register your models here.
admin.site.register(Facility)
admin.site.register(Manufacturer)
admin.site.register(Vaccine)
admin.site.register(Vaccination)
