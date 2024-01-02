from rest_framework import serializers
from .models import Flight, TicketReservation ,UserPreferences ,Airport ,FlightReview
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'birth_date', 'address']


class TicketReservationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    seat_preference = serializers.CharField(max_length=10, allow_blank=True, required=False)
    additional_services = serializers.ListField(child=serializers.CharField(max_length=50), allow_empty=True, required=False)

    class Meta:
        model = TicketReservation
        fields = ['id', 'user', 'passenger_name', 'passenger_email', 'reservation_date', 'number_of_passengers', 'payment_info', 'booking_confirmation', 'flight', 'seat_preference', 'additional_services']

    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data['user'] = user
        return super().create(validated_data)

class UserPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPreferences
        fields = '__all__'

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'
class FlightReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightReview
        fields = '__all__'

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Flight
        fields = '__all__'
