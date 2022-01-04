from rest_framework import serializers
from api.models import User, Rooms, Course, Reservation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ['location', 'title', 'type', 'contact', 'is_booked']


class CourseSerializer(serializers.ModelSerializer):
    room_img1 = serializers.ImageField(use_url=True)
    room_img2 = serializers.ImageField(use_url=True)
    room_img3 = serializers.ImageField(use_url=True)
    meal_img1 = serializers.ImageField(use_url=True)
    meal_img2 = serializers.ImageField(use_url=True)
    meal_img3 = serializers.ImageField(use_url=True)
    meal_img4 = serializers.ImageField(use_url=True)
    meal_img5 = serializers.ImageField(use_url=True)
    meal_img6 = serializers.ImageField(use_url=True)
    act_img1 = serializers.ImageField(use_url=True)
    act_img2 = serializers.ImageField(use_url=True)
    act_img3 = serializers.ImageField(use_url=True)
    result_img = serializers.ImageField(use_url=True)

    class Meta:
        model = Course
        fields = ['city', 'partner', 'room_name', 'room_detail', 'room_hash', 'room_img1', 'room_img2', 'room_img3',
                  'meal_name1', 'meal_detail1', 'meal_hash1', 'meal_img1', 'meal_name2', 'meal_detail2', 'meal_hash2',
                  'meal_img2', 'meal_name3', 'meal_detail3', 'meal_hash3', 'meal_img3', 'meal_name4', 'meal_detail4',
                  'meal_hash4', 'meal_img4', 'meal_name5', 'meal_detail5', 'meal_hash5', 'meal_img5', 'meal_name6',
                  'meal_detail6', 'meal_hash6', 'meal_img6', 'act_name1', 'act_detail1', 'act_hash1', 'act_img1',
                  'act_name2', 'act_detail2', 'act_hash2', 'act_img2', 'act_name3', 'act_detail3', 'act_hash3',
                  'act_img3', 'price', 'result_img']


class ReservationSerializer(serializers.ModelSerializer):
    course = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Reservation
        fields = '__all__'
