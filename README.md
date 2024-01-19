# Django Flight Reservation Project

This Django project is designed for managing flight reservations, user preferences, and reviews, with integrated PayPal payment functionality. Below is a breakdown of the project structure:

## Models

### TicketReservation
Represents a reservation with details like the user, passenger information, reservation date, etc.

### Airport
Represents an airport with a code, name, city, and country.

### UserPreferences
Represents user preferences such as a favorite airline and preferred seat.

### Flight
Represents a flight with details like airline, departure, arrival, price, and duration.

### Airline
Represents an airline with a name, code, and an optional logo.

### FlightReview
Represents a user review for a specific flight.

## Serializers

### UserSerializer
Serializes user-related information.

### TicketReservationSerializer
Serializes ticket reservation data, including nested serializers for user and flight.

### UserPreferencesSerializer
Serializes user preferences.

### AirportSerializer
Serializes airport data.

### FlightReviewSerializer
Serializes flight review data.

### FlightSerializer
Serializes flight-related information.

## Views

### get_flights
Retrieves a list of flights.

### get_reservations
Retrieves a list of reservations.

### FlightListCreateView and FlightDetailView
API views for listing and managing flights.

### TicketReservationListCreateView and TicketReservationDetailView
API views for listing and managing reservations.

### FlightReviewView
Views for creating and managing flight reviews.

### UserBookingsView
Retrieves bookings for a specific user.

### view_reservation_history
Retrieves reservation history for the authenticated user.

### cancel_reservation
Cancels a reservation.

### modify_reservation
Modifies a reservation.

### initiate_paypal_payment, paypal_payment_success, paypal_payment_cancel
Handles PayPal payment integration.

### user_preferences_view
Retrieves and updates user preferences.

### airport_list_view
Retrieves a list of airports.

## Middleware

### TokenAuthMiddleware
Custom middleware for handling token-based authentication.

## Celery

Uses Celery for handling background tasks. The configuration is set up in the celery.py file.

This project aims to provide a comprehensive solution for managing flight reservations, ensuring a seamless experience for both users and administrators.


 ```


-The project is now accessible at http://localhost:8000/. Make sure to set up necessary environment variables, such as PayPal credentials, before running the project.
