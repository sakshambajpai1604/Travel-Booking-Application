from django.test import TestCase
from django.contrib.auth.models import User
from .models import TravelOption, Booking
from django.utils import timezone

class TravelOptionModelTest(TestCase):
    def test_create_travel_option(self):
        option = TravelOption.objects.create(
            type='Flight',
            source='CityA',
            destination='CityB',
            date_time=timezone.now(),
            price=100.00,
            available_seats=50
        )
        self.assertEqual(option.type, 'Flight')
        self.assertEqual(option.available_seats, 50)

class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.option = TravelOption.objects.create(
            type='Bus',
            source='CityX',
            destination='CityY',
            date_time=timezone.now(),
            price=50.00,
            available_seats=20
        )

    def test_create_booking(self):
        booking = Booking.objects.create(
            user=self.user,
            travel_option=self.option,
            number_of_seats=2,
            total_price=100.00
        )
        self.assertEqual(booking.number_of_seats, 2)
        self.assertEqual(booking.status, 'Confirmed')
        self.assertEqual(booking.total_price, 100.00)
