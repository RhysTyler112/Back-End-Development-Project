from django.contrib import admin
from django.utils.html import format_html
from .models import GymClass, Booking, Membership

class GymClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time', 'edit_button', 'delete_button')

    def edit_button(self, obj):
        # Generates an Edit link for the object
        return format_html('<a class="btn btn-primary btn-sm" href="{}">Edit</a>', 
                           f'/admin/app_name/gymclass/{obj.id}/change/')

    def delete_button(self, obj):
        # Generates a Delete link for the object
        return format_html('<a class="btn btn-danger btn-sm" href="{}">Delete</a>', 
                           f'/admin/app_name/gymclass/{obj.id}/delete/')

    edit_button.short_description = 'Edit'
    delete_button.short_description = 'Delete'

class BookingAdmin(admin.ModelAdmin):
    list_display = ('gym_class', 'user', 'edit_button', 'delete_button')

    def edit_button(self, obj):
        # Generates an Edit link for the object
        return format_html('<a class="btn btn-primary btn-sm" href="{}">Edit</a>', 
                           f'/admin/app_name/booking/{obj.id}/change/')

    def delete_button(self, obj):
        # Generates a Delete link for the object
        return format_html('<a class="btn btn-danger btn-sm" href="{}">Delete</a>', 
                           f'/admin/app_name/booking/{obj.id}/delete/')

    edit_button.short_description = 'Edit'
    delete_button.short_description = 'Delete'
# Register your models here.
admin.site.register(Membership)
admin.site.register(GymClass, GymClassAdmin)
admin.site.register(Booking, BookingAdmin)