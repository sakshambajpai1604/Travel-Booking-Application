from django import forms

class BookingForm(forms.Form):
    number_of_seats = forms.IntegerField(min_value=1, label="Number of Seats")