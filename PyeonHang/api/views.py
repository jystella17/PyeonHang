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

    def get(self, request, id, *args, **kwargs):
        course_id = get_object_or_404(Course, pk=id)
        detail = Course.objects.filter(id=course_id).values()

        return Response({'detail': detail}, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        user = get_object_or_404(User, )
        course = Course()
        serializer = self.get_serializer(data=request.data, **kwargs)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RandomCourse(generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # permission_classes = (IsSuperUserOrReadOnly,)

    @staticmethod
    def get(request, partner, *args, **kwargs):
        print(partner)
        loc = ['강릉', '속초', '서울', '여수', '전주', '전주', '울릉도', '남해', '통영', '냠원']
        rand = random.choice(loc)
        random_course = Course.objects.filter(city=rand).filter(partner=partner).values()

        return Response({'course': random_course}, status=status.HTTP_200_OK)


class ReservationView(generics.GenericAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def post(self, request, *args, **kwargs):
        return Response()
