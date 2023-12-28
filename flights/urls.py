from django.urls import path
from .views import *

urlpatterns = [
    path('flights/', FlightListCreateView.as_view(), name='flight-list-create'),
    path('flights/<int:pk>/', FlightDetailView.as_view(), name='flight-detail'),
    path('reservations/', TicketReservationListCreateView.as_view(), name='reservation-list-create'),
    path('reservations/<int:pk>/', TicketReservationDetailView.as_view(), name='reservation-detail'),
     path('api/reservations/history/', view_reservation_history, name='view_reservation_history'),
    path('api/reservations/<int:reservation_id>/cancel/', cancel_reservation, name='cancel_reservation'),
    path('api/reservations/<int:reservation_id>/modify/', modify_reservation, name='modify_reservation'),
 path('api/paypal/initiate-payment/<int:reservation_id>/', initiate_paypal_payment, name='initiate-paypal-payment'),
    path('api/paypal/payment-success/', paypal_payment_success, name='paypal-payment-success'),
    path('api/paypal/payment-cancel/', paypal_payment_cancel, name='paypal-payment-cancel'),

]
 
