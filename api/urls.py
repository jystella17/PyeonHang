from . import views
from django.urls import include, path
from rest_framework import routers


router = routers.DefaultRouter()
router.register('rooms', views.RoomViewSet)
router.register('room-price', views.RoomPriceViewSet)
router.register('sample-data', views.SampleDataViewSet)
router.register('course', views.CourseViewSet)
router.register('course-price', views.CoursePriceViewSet)
router.register('payment', views.PaymentViewSet)
router.register('reservation', views.ReservationViewSet)

urlpatterns = [
    path('', include(router.urls))
]