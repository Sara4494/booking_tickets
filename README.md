
Flight Reservation System
This Django project provides a simple flight reservation system with RESTful API endpoints. The system allows users to view available flights, make reservations, and manage their reservation history.

Models
Flight Model (flights.models.Flight):

Represents a flight with attributes such as departure_city, destination_city, departure_date, arrival_date, and price.
TicketReservation Model (flights.models.TicketReservation):

Represents a user's reservation with attributes like user, flight, passenger_name, passenger_email, reservation_date, number_of_passengers, payment_info, and booking_confirmation.
API Endpoints
Get Flights (GET /api/flights/):

Retrieves a list of available flights.
Get Reservations (GET /api/reservations/):

Retrieves a list of user reservations.
Filter Flights (GET /api/flights/?departure_city=&destination_city=&min_price=&max_price=&departure_date=):

Allows filtering flights based on various parameters such as departure_city, destination_city, min_price, max_price, and departure_date.
Flight Detail (GET /api/flights/<flight_id>/, PUT /api/flights/<flight_id>/, DELETE /api/flights/<flight_id>/):

Retrieves, updates, or deletes details of a specific flight.
Reservation Detail (GET /api/reservations/<reservation_id>/, PUT /api/reservations/<reservation_id>/, DELETE /api/reservations/<reservation_id>/):

Retrieves, updates, or deletes details of a specific reservation.
List/Create Flights (GET /api/flights/, POST /api/flights/):

Lists all flights or creates a new flight.
List/Create Reservations (GET /api/reservations/, POST /api/reservations/):

Lists all reservations or creates a new reservation.
View Reservation History (GET /api/reservations/history/):

Retrieves the reservation history for the logged-in user.
Cancel Reservation (POST /api/reservations/<reservation_id>/cancel/):

Cancels a specific reservation.
Modify Reservation (PUT /api/reservations/<reservation_id>/modify/):

Modifies details of a specific reservation.
Initiate PayPal Payment (POST /api/paypal/initiate-payment/<reservation_id>/):

Initiates a PayPal payment for a reservation.
PayPal Payment Success (GET /api/paypal/payment-success/):

Handles successful PayPal payments.
PayPal Payment Cancel (GET /api/paypal/payment-cancel/):

Handles canceled PayPal payments.
Middleware
Custom Exception Handler Middleware (flights.middleware.CustomExceptionHandlerMiddleware):
Catches exceptions and returns a JSON response with an error message.
Celery
Celery Configuration (CELERY_BROKER_URL = 'redis://localhost:6379/0'):
Uses Celery with Redis as the message broker for handling asynchronous tasks.
Email Configuration
Email Configuration (settings.EMAIL_...):
Configures Gmail as the email backend for sending reservation confirmation emails.
PayPal Integration
PayPal Configuration (settings.PAYPAL_...):
Configures PayPal credentials for processing payments.
Dependencies
Django REST Framework (rest_framework):

Used for building the API.
Celery (celery):

Used for handling asynchronous tasks.
PayPal REST SDK (paypalrestsdk):

Used for integrating PayPal payments.
Running the Project
Clone the repository:

bash
Copy code
git clone <repository_url>
Install dependencies:

Copy code
pip install -r requirements.txt
Apply migrations:

Copy code
python manage.py migrate
Run the development server:

Copy code
python manage.py runserver
The project is now accessible at http://localhost:8000/. Make sure to set up necessary environment variables, such as PayPal credentials, before running the project.
