from django.db import models
 
from django.conf import settings
 

class Flight(models.Model):
    departure_city = models.CharField(max_length=100, verbose_name="Departure City")
    destination_city = models.CharField(max_length=100, verbose_name="Destination City")
    departure_date = models.DateTimeField(auto_now_add=True)
    arrival_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.departure_city} to {self.destination_city}"

 

class TicketReservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User")
    flight = models.ForeignKey('Flight', on_delete=models.CASCADE, verbose_name="Flight")
    passenger_name = models.CharField(max_length=100)
    passenger_email = models.EmailField()
    reservation_date = models.DateTimeField(auto_now_add=True)
    number_of_passengers = models.PositiveIntegerField(default=1)
    payment_info = models.TextField(blank=True, null=True)   
    booking_confirmation = models.BooleanField(default=False)  

    def __str__(self):
        return f"{self.passenger_name} on {self.flight.departure_city} to {self.flight.destination_city}"
