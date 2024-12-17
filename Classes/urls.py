from . import views
from django.urls import path

urlpatterns = [
    path('', views.ClassesList.as_view(), name='home'),
     path('New Booking/', views.create_booking, name='booking_create'),
]