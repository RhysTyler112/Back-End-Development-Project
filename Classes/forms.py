from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'first_name',
            'last_name',
            'email',
            'gym_class',
            'experience_level',
            'further_information']

    def clean_gym_class(self):
        gym_class = self.cleaned_data.get('gym_class')
        if not gym_class:
            raise forms.ValidationError("You must select a class before submitting the form.")
        return gym_class