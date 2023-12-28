from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status ,generics
from .models import Flight, TicketReservation
from .serializers import FlightSerializer, TicketReservationSerializer
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.translation import gettext_lazy as _
from django.shortcuts import get_object_or_404, render
from paypalrestsdk import Payment

@api_view(['GET'])
def get_flights(request):
    try:
        flights = Flight.objects.all()
        serializer = FlightSerializer(flights, many=True)
        return Response({
            'status': _('success'),
            'message': _('Flights retrieved successfully'),
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'status': _('error'),
            'message': _('Error retrieving flights: {}').format(str(e))
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_reservations(request):
    try:
        reservations = TicketReservation.objects.all()
        serializer = TicketReservationSerializer(reservations, many=True)
        return Response({
            'status': _('success'),
            'message': _('Reservations retrieved successfully'),
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'status': _('error'),
            'message': _('Error retrieving reservations: {}').format(str(e))
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

 

class FlightListCreateView(generics.ListCreateAPIView):
    serializer_class = FlightSerializer

    def get_queryset(self):
        queryset = Flight.objects.all()

  
        departure_city = self.request.query_params.get('departure_city', None)
        destination_city = self.request.query_params.get('destination_city', None)
        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)
        departure_date = self.request.query_params.get('departure_date', None)
 
        if departure_city:
            queryset = queryset.filter(departure_city=departure_city)
        if destination_city:
            queryset = queryset.filter(destination_city=destination_city)
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        if departure_date:
            queryset = queryset.filter(departure_date__gte=departure_date)

        return queryset

    def list(self, request, *args, **kwargs):
        try:
            flights = self.get_queryset()
            serializer = self.serializer_class(flights, many=True)
            return Response({
                'status': 'success',
                'message': 'Flights retrieved successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Error retrieving flights: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class FlightDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.serializer_class(instance)
            return Response({
                'status': 'success',
                'message': 'Flight retrieved successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Error retrieving flight: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.serializer_class(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                'status': 'success',
                'message': 'Flight updated successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Error updating flight: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return Response({
                'status': 'success',
                'message': 'Flight deleted successfully'
            }, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Error deleting flight: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TicketReservationListCreateView(generics.ListCreateAPIView):
    queryset = TicketReservation.objects.all()
    serializer_class = TicketReservationSerializer

    def list(self, request, *args, **kwargs):
        try:
            reservations = self.get_queryset()
            serializer = self.serializer_class(reservations, many=True)
            return Response({
                'status': 'success',
                'message': 'Reservations retrieved successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Error retrieving reservations: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                'status': 'success',
                'message': 'Reservation created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Error creating reservation: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TicketReservationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TicketReservation.objects.all()
    serializer_class = TicketReservationSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.serializer_class(instance)
            return Response({
                'status': 'success',
                'message': 'Reservation retrieved successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Error retrieving reservation: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.serializer_class(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

           
            self.send_confirmation_email(instance)

            return Response({
                'status': 'success',
                'message': 'Reservation updated successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Error updating reservation: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def send_confirmation_email(self, reservation):
        try:
            subject = 'تأكيد الحجز'
            message = f'شكرًا لحجز تذكرتك. رقم الحجز: {reservation.id}.'

    
            html_message = render_to_string('confirmation_email_template.html', {'reservation': reservation}) or 'Default HTML message'

            plain_message = strip_tags(html_message)

            from_email = 'riad52166@gmail.com'
            to_email = reservation.passenger_email

            send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)
        except Exception as e:
            print(f"Error rendering HTML message: {e}")
 
def custom_error_page(request, exception=None):
    return render(request, 'error_page.html', status=500)

 
 

@api_view(['GET'])
def view_reservation_history(request):
    user = request.user
    reservations = TicketReservation.objects.filter(user=user)
    serializer = TicketReservationSerializer(reservations, many=True)
    return Response({
        'status': 'success',
        'message': 'Reservation history retrieved successfully',
        'data': serializer.data
    }, status=status.HTTP_200_OK)

 
@api_view(['POST'])
def cancel_reservation(request, reservation_id):
    try:
        reservation = TicketReservation.objects.get(id=reservation_id, user=request.user)
 
        reservation.delete()  

        return Response({
            'status': 'success',
            'message': 'Reservation cancelled successfully',
            'data': None
        }, status=status.HTTP_200_OK)
    except TicketReservation.DoesNotExist:
        return Response({
            'status': 'error',
            'message': 'Reservation not found',
            'data': None
        }, status=status.HTTP_404_NOT_FOUND)

 
@api_view(['PUT'])
def modify_reservation(request, reservation_id):
    try:
        reservation = TicketReservation.objects.get(id=reservation_id, user=request.user)
        serializer = TicketReservationSerializer(instance=reservation, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'status': 'success',
            'message': 'Reservation modified successfully',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    except TicketReservation.DoesNotExist:
        return Response({
            'status': 'error',
            'message': 'Reservation not found',
            'data': None
        }, status=status.HTTP_404_NOT_FOUND)


 
 
@api_view(['POST'])
def initiate_paypal_payment(request, reservation_id):
    reservation = get_object_or_404(TicketReservation, id=reservation_id)

    payment = Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal",
        },
         "redirect_urls": {
        "return_url": "http://yourdomain.com/api/paypal/payment-success/",   
        "cancel_url": "http://yourdomain.com/api/paypal/payment-cancel/",  
        },
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": f"Flight Reservation - {reservation.flight.departure_city} to {reservation.flight.destination_city}",
                    "sku": "reservation",
                    "quantity": reservation.number_of_passengers,
                    "price": str(reservation.flight.price),
                    "currency": "USD",   
                }],
            },
            "amount": {
                "total": str(reservation.flight.price * reservation.number_of_passengers),
                "currency": "USD",  
            },
            "description": "Flight Reservation Payment",
        }],
    })

    if payment.create():
         
        request.session['reservation_id'] = reservation_id
        return Response({"payment_url": payment.links[1].href})
    else:
        return Response({"error": payment.error})


@api_view(['GET'])
def paypal_payment_success(request):
    payment_id = request.query_params.get('paymentId')
    payer_id = request.query_params.get('PayerID')

    payment = Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        
        reservation_id = request.session.get('reservation_id')   
        reservation = get_object_or_404(TicketReservation, id=reservation_id)
 
        reservation.booking_confirmation = True
        reservation.save()

        return Response({"message": "Payment successful. Reservation confirmed."})
    else:
        return Response({"error": payment.error})

@api_view(['GET'])
def paypal_payment_cancel(request):
  
    return Response({"message": "Payment canceled. Reservation not confirmed."})