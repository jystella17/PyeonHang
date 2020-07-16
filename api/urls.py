from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register('rooms', views.RoomViewSet)
router.register('room-price', views.RoomPriceViewSet)
router.register('sample-data', views.SampleDataViewSet)
router.register('course', views.CourseViewSet)
router.register('course-price', views.CoursePriceViewSet)
router.register('payment', views.PaymentViewSet)
router.register('reservation', views.ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
