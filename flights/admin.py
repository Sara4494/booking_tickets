from django.contrib import admin
from .models import *
admin.site.register(Flight)
admin.site.register(TicketReservation)
admin.site.register(Airport)
admin.site.register(Airline)
admin.site.register(UserPreferences)
admin.site.register(FlightReview)
