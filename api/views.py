from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from api.serializers import *
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, filters
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


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (IsNotAnonymous,)


class RoomPriceViewSet(viewsets.ModelViewSet):
    queryset = RoomPrice.objects.all()
    serializer_class = RoomPriceSerializer
    permission_classes = (IsNotAnonymous,)


class SampleDataViewSet(viewsets.ModelViewSet):
    queryset = SampleData.objects.all()
    serializer_class = SampleDataSerializer
    permission_classes = (IsSuperUserOrReadOnly,)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsSuperUserOrReadOnly,)

    '''
    @action(methods=['get'], detail=False, url_path='recommend', url_name='recommend')
    def random_course(self, request, *args, **kwargs):
        loc = ['Gangneung', 'Sokcho', 'Seoul', 'Yeosu', 'Jeonju', 'Jeju', 'Ulleungdo', 'Namhae', 'Tongyeong', 'Namwon']
        rand = random.choice(loc)
        d = Course.objects.filter(city=rand).values()
        data = list(d)
        return JsonResponse(data)
    '''


class CoursePriceViewSet(viewsets.ModelViewSet):
    queryset = CoursePrice.objects.all()
    serializer_class = CoursePriceSerializer
    permission_classes = (IsSuperUserOrReadOnly,)


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = (IsSuperUserOrReadOnly,)


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (IsSuperUserOrReadOnly,)
