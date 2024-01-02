from django.urls import path
from flights.views import booking_history,UserBookingsView,FlightDetailView ,FlightListCreateView , TicketReservationDetailView ,TicketReservationListCreateView ,view_reservation_history ,cancel_reservation ,modify_reservation ,initiate_paypal_payment ,paypal_payment_cancel ,paypal_payment_success

urlpatterns = [
    path('flights_list/', FlightListCreateView.as_view(), name='flight-list-create'),
    path('flights/<int:pk>/', FlightDetailView.as_view(), name='flight-detail'),
    path('reservations/', TicketReservationListCreateView.as_view(), name='reservation-list-create'),
    path('reservations/<int:pk>/', TicketReservationDetailView.as_view(), name='reservation-detail'),
     path('api/reservations/history/', view_reservation_history, name='view_reservation_history'),
    path('api/reservations/<int:reservation_id>/cancel/', cancel_reservation, name='cancel_reservation'),
    path('api/reservations/<int:reservation_id>/modify/', modify_reservation, name='modify_reservation'),
 path('api/paypal/initiate-payment/<int:reservation_id>/', initiate_paypal_payment, name='initiate-paypal-payment'),
    path('api/paypal/payment-success/', paypal_payment_success, name='paypal-payment-success'),
    path('api/paypal/payment-cancel/', paypal_payment_cancel, name='paypal-payment-cancel'),
    path('user/bookings/', UserBookingsView.as_view(), name='user-bookings'),
    path('booking-history/', booking_history, name='booking-history'),

]
 
