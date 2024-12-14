from django.contrib import admin
from .models import Membership, GymClass, Booking

# Register your models here.
admin.site.register(Membership)
admin.site.register(GymClass)
admin.site.register(Booking)