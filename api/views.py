from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from api.serializers import *
from api.models import User
from rest_framework import viewsets, status, permissions, generics
from rest_framework.decorators import action
import random


SAFE_METHODS = ['GET', 'OPTIONS', 'HEAD']


class IsSuperUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser


class IsNotAnonymous(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False


class CourseDetail(generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # permission_classes = (IsSuperUserOrReadOnly,)

    def get(self, request, id,  *args, **kwargs):
        course_id = get_object_or_404(Course, pk=id)
        detail = Course.objects.filter(id=course_id).values()

        return Response({'detail': detail}, status=status.HTTP_200_OK)


class CourseRegister(generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User)
        if not user.is_superuser:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        course = Course()
        serializer = self.get_serializer(data=request.data, **kwargs)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RandomCourse(generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # permission_classes = (IsSuperUserOrReadOnly,)

    def get(self, request, partner, *args, **kwargs):
        loc = ['강릉', '속초', '서울', '여수', '전주', '전주', '울릉도', '남해', '통영', '남원']
        rand = random.choice(loc)
        random_course = Course.objects.filter(city=rand).filter(partner=partner).values()

        return Response({'course': random_course}, status=status.HTTP_200_OK)


class MakeReservation(generics.GenericAPIView):
    queryset_res = Reservation.objects.all()
    queryset_room = Rooms.objects.all()
    serializer_class_res = ReservationSerializer
    serializer_class_room = RoomSerializer

    def post(self, request, *args, **kwargs):
        city = request.data['city']
        partner = request.data['partner']
        course = Course.objects.get(Q(city=city) & Q(partner=partner))
        price = course.price
        reservation = Reservation(
            username=request.data['username'],
            phone=request.data['phone_num'],
            email=request.data['email'],
            res_course=course,
            date=request.data['booking_date'],
            payment=price
        )
        reservation.save()

        room = course.room_name
        user_email = request.data['email']
        user_email = Reservation.objects.get(email=user_email)
        date = request.data['booking_date']
        room_res = RoomReservation(
            room=room,
            booked_by=user_email,
            booked_date=date
        )
        room_res.save()

        return Response(status=status.HTTP_201_CREATED)


class ReservationList(generics.GenericAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def post(self, request, *args, **kwargs):
        username = request.data["name"]
        phone = request.data["phone_num"]
        email = request.data["email"]
        reservation = Reservation.objects.filter(username=username).filter(phone=phone).filter(email=email).values()

        return Response({"reservation": reservation}, status=status.HTTP_200_OK)
