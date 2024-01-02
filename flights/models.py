 
from django.db import models
from django.contrib.auth import get_user_model

from django.utils.translation import gettext_lazy as _

class TicketReservation(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    passenger_name = models.CharField(max_length=255)
    passenger_email = models.EmailField()
    reservation_date = models.DateTimeField(auto_now_add=True)
    number_of_passengers = models.PositiveIntegerField()
    payment_info = models.TextField()
    booking_confirmation = models.BooleanField(default=False)
    flight = models.ForeignKey('Flight', on_delete=models.CASCADE)
    seat_preference = models.CharField(max_length=10, blank=True, null=True)
    additional_services = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Reservation {self.id} - {self.user.username}"
class Airport(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.code})"

class UserPreferences(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    favorite_airline = models.CharField(max_length=100, blank=True, null=True)
    preferred_seat = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"Preferences for {self.user.username}"

class Flight(models.Model):
    airline = models.ForeignKey('Airline', on_delete=models.CASCADE)
    departure_airport = models.ForeignKey('Airport', related_name='departure_flights', on_delete=models.CASCADE)
    arrival_airport = models.ForeignKey('Airport', related_name='arrival_flights', on_delete=models.CASCADE)
    departure_date = models.DateTimeField()
    arrival_date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seats = models.PositiveIntegerField()
    duration = models.DurationField()
    departure_city = models.CharField(max_length=255,blank=True, null=True)
    destination_city = models.CharField(max_length=255, blank=True, null=True)
  
    aircraft_type = models.CharField(max_length=50, blank=True, null=True)
    flight_services = models.TextField(blank=True, null=True)
    is_wifi_available = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.airline.name} to {self.departure_airport.name}"

class Airline(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3)
    logo = models.ImageField(upload_to='airline_logos/', blank=True, null=True)

    def __str__(self):
        return self.name

class FlightReview(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    flight = models.ForeignKey('Flight', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Review by {self.user.username} for Flight {self.flight.id}"
