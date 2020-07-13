from rest_framework import serializers
from api.models import Rooms, RoomPrice, SampleData, Course, CoursePrice, Payment, Reservation


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ['location', 'title', 'type', 'contact', 'is_booked']


class RoomPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomPrice
        fields = ['room', 'price']


class SampleDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleData
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CoursePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursePrice
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['room_price', 'activity_price']


class ReservationSerializer(serializers.ModelSerializer):
    course = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Reservation
        fields = '__all__'
