from django import forms
from django.contrib.auth.models import User

class BookingForm(forms.Form):
    number_of_seats = forms.IntegerField(min_value=1, label="Number of Seats")

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']