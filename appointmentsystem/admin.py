from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(AppointmentNew)
admin.site.register(beverage)
admin.site.register(service)
admin.site.register(complementarydrink)
admin.site.register(barber)