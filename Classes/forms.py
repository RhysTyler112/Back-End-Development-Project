from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['gym_class', 'equipment_needed', 'experience_level', 'further_information']