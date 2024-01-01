from rest_framework import serializers
from .models import Flight, TicketReservation
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'birth_date', 'address']

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
class TicketReservationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = TicketReservation
        fields = ['id', 'user', 'passenger_name', 'passenger_email', 'reservation_date', 'number_of_passengers', 'payment_info', 'booking_confirmation', 'flight']

    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data['user'] = user
        return super().create(validated_data)