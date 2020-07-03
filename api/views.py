from django.shortcuts import render
from rest_framework.response import Response
from api.serializers import *
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, filters


SAFE_METHODS = ['GET', 'OPTIONS', 'HEAD']


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = RoomSerializer


class RoomPriceViewSet(viewsets.ModelViewSet):
    queryset = RoomPrice.objects.all()
    serializer_class = RoomPriceSerializer


class SampleDataViewSet(viewsets.ModelViewSet):
    queryset = SampleData.objects.all()
    serializer_class = SampleDataSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CoursePriceViewSet(viewsets.ModelViewSet):
    queryset = CoursePrice.objects.all()
    serializer_class = CoursePriceSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
