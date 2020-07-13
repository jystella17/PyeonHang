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

    @action(methods=['get'], detail=False, url_path='recommend', url_name='recommend')
    def random_course(self, request, *args, **kwargs):
        loc = ['Gangneung', 'Sokcho', 'Seoul', 'Yeosu', 'Jeonju', 'Jeju', 'Ulleungdo', 'Namhae', 'Tongyeong', 'Namwon']
        rand = random.choice(loc)
        d = Course.objects.filter(city=rand).values()
        data = list(d)
        return JsonResponse(data)

        '''
            for i in range(0, 3):
            self.queryset = Course.objects.filter(pk=num).values()
            to = Course.objects.filter(pk=num).value('city')
            who = Course.objects.filter(pk=num).value('partner')

            r_name = Course.objects.filter(pk=num).value('room_name')
            r_detail = Course.objects.filter(pk=num).value('room_detail')
            r_hash = Course.objects.filter(pk=num).value('room_hash')
            r_img1 = Course.objects.filter(pk=num).value('room_img1')
            r_img2 = Course.objects.filter(pk=num).value('room_img2')
            r_img3 = Course.objects.filter(pk=num).value('room_img3')

            m_name1 = Course.objects.filter(pk=num).value('meal_name1')
            m_detail1 = Course.objects.filter(pk=num).value('meal_detail1')
            m_hash1 = Course.objects.filter(pk=num).value('meal_hash1')
            m_img1 = Course.objects.filter(pk=num).value('meal_img1')

            m_name2 = Course.objects.filter(pk=num).value('meal_name2')
            m_detail2 = Course.objects.filter(pk=num).value('meal_detail2')
            m_hash2 = Course.objects.filter(pk=num).value('meal_hash2')
            m_img2 = Course.objects.filter(pk=num).value('meal_img2')

            m_name3 = Course.objects.filter(pk=num).value('meal_name3')
            m_detail3 = Course.objects.filter(pk=num).value('meal_detail3')
            m_hash3 = Course.objects.filter(pk=num).value('meal_hash3')
            m_img3 = Course.obejcts.filter(pk=num).value('meal_img3')

            m_name4 = Course.objects.filter(pk=num).value('meal_name4')
            m_detail4 = Course.objects.filter(pk=num).value('meal_detail4')
            m_hash4 = Course.objects.filter(pk=num).value('meal_hash4')
            m_img4 = Course.obejcts.filter(pk=num).value('meal_img4')

            m_name5 = Course.objects.filter(pk=num).value('meal_name5')
            m_detail5 = Course.objects.filter(pk=num).value('meal_detail5')
            m_hash5 = Course.objects.filter(pk=num).value('meal_hash5')
            m_img5 = Course.obejcts.filter(pk=num).value('meal_img5')

            m_name6 = Course.objects.filter(pk=num).value('meal_name6')
            m_detail6 = Course.objects.filter(pk=num).value('meal_detail6')
            m_hash6 = Course.objects.filter(pk=num).value('meal_hash6')
            m_img6 = Course.obejcts.filter(pk=num).value('meal_img6')

            a_name1 = Course.objects.filter(pk=num).value('act_name1')
            a_detail1 = Course.objects.filter(pk=num).value('act_detail1')
            a_hash1 = Course.objects.filter(pk=num).value('act_hash1')
            a_img1 = Course.objects.filter(pk=num).value('act_img1')

            a_name2 = Course.objects.filter(pk=num).value('act_name2')
            a_detail2 = Course.objects.filter(pk=num).value('act_detail2')
            a_hash2 = Course.objects.filter(pk=num).value('act_hash2')
            a_img2 = Course.objects.filter(pk=num).value('act_img2')

            a_name3 = Course.objects.filter(pk=num).value('act_name3')
            a_detail3 = Course.objects.filter(pk=num).value('act_detail3')
            a_hash3 = Course.objects.filter(pk=num).value('act_hash3')
            a_img3 = Course.objects.filter(pk=num).value('act_img3')

            result = Course.objects.filter(pk=num).value('result_img')

            data = {
                "city": to,
                "partner": who,
                "room_name": r_name,
                "room_detail": r_detail,
                "room_hash": r_hash,
                "room_img1": r_img1,
                "room_img2": r_img2,
                "room_img3": r_img3,

                "meal_name1": m_name1,
                "meal_detail1": m_detail1,
                "meal_hash1": m_hash1,
                "meal_img1": m_img1,

                "meal_name2": m_name2,
                "meal_detail2": m_detail2,
                "meal_hash2": m_hash2,
                "meal_img2": m_img2,

                "meal_name3": m_name3,
                "meal_detail3": m_detail3,
                "meal_hash3": m_hash3,
                "meal_img3": m_img3,

                "meal_name4": m_name4,
                "meal_detail4": m_detail4,
                "meal_hash4": m_hash4,
                "meal_img4": m_img4,

                "meal_name5": m_name5,
                "meal_detail5": m_detail5,
                "meal_hash5": m_hash5,
                "meal_img5": m_img5,

                "meal_name6": m_name6,
                "meal_detail6": m_detail6,
                "meal_hash6": m_hash6,
                "meal_img6": m_img6,

                "act_name1": a_name1,
                "act_detail1": a_detail1,
                "act_hash1": a_hash1,
                "act_img1": a_img1,

                "act_name2": a_name2,
                "act_detail2": a_detail2,
                "act_hash2": a_hash2,
                "act_img2": a_img2,

                "act_name3": a_name3,
                "act_detail3": a_detail3,
                "act_hash3": a_hash3,
                "act_img3": a_img3,

                "result_img": result
            }
            num = num+10
            return JsonResponse(data)
        return HttpResponse
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
