from django.contrib import admin
from .models import Contact, Registration, Booking, Car

# Register your models here.
admin.site.register(Registration)
admin.site.register(Contact)
admin.site.register(Booking)
admin.site.register(Car)

