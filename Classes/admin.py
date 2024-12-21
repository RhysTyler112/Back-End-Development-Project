from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import GymClass, Booking, Membership

class GymClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time', 'edit_button', 'delete_button')

    def edit_button(self, obj):
        # Generate the URL for the edit page dynamically
        edit_url = reverse('admin:Classes_gymclass_change', args=[obj.id])
        return format_html('<a class="btn btn-primary btn-sm" href="{}">Edit</a>', edit_url)

    def delete_button(self, obj):
        # Generate the URL for the delete page dynamically
        delete_url = reverse('admin:Classes_gymclass_delete', args=[obj.id])
        return format_html('<a class="btn btn-danger btn-sm" href="{}">Delete</a>', delete_url)

    edit_button.short_description = 'Edit'
    delete_button.short_description = 'Delete'

class BookingAdmin(admin.ModelAdmin):
    list_display = ('gym_class', 'user', 'edit_button', 'delete_button')

    def edit_button(self, obj):
        # Generate the URL for the edit page dynamically
        edit_url = reverse('admin:Classes_booking_change', args=[obj.id])
        return format_html('<a class="btn btn-primary btn-sm" href="{}">Edit</a>', edit_url)

    def delete_button(self, obj):
        # Generate the URL for the delete page dynamically
        delete_url = reverse('admin:Classes_booking_delete', args=[obj.id])
        return format_html('<a class="btn btn-danger btn-sm" href="{}">Delete</a>', delete_url)

    edit_button.short_description = 'Edit'
    delete_button.short_description = 'Delete'
# Register your models here.
admin.site.register(Membership)
admin.site.register(GymClass, GymClassAdmin)
admin.site.register(Booking, BookingAdmin)