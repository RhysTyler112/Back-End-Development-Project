from . import views
from django.urls import path

urlpatterns = [
    path('', views.ClassesList.as_view(), name='home'),
    path('bookings/', views.BookingListView.as_view(), name='booking_list'),
    path('new-booking/<int:gym_class_id>/', views.newBooking, name='new_booking'),
]