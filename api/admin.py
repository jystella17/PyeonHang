from django.contrib import admin
from .models import *


class RoomAdmin(admin.ModelAdmin):
    list_display = ['location', 'title', 'type', 'contact', 'is_booked']


class RoomPriceAdmin(admin.ModelAdmin):
    list_display = ['room_name', 'price']


class SampleDataAdmin(admin.ModelAdmin):
    list_display = ['city', 'sample_img1', 'sample_img2']


class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'city', 'partner', 'room_img1', 'room_img2', 'room_img3', 'meal_img1', 'meal_img2',
        'meal_img3', 'meal_img4', 'meal_img5', 'meal_img6', 'act_img1', 'act_img2', 'act_img3', 'act_img4',
        'act_img5', 'act_img6'
    ]


class CoursePriceAdmin(admin.ModelAdmin):
    list_display = ['destination', 'activity']


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['room_price', 'activity_price']


class ReservationAdmin(admin.ModelAdmin):
    list_display = ['username', 'phone', 'email', 'res_course', 'date', 'pay']


admin.site.register(Rooms, RoomAdmin)
admin.site.register(RoomPrice, RoomPriceAdmin)
admin.site.register(SampleData, SampleDataAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(CoursePrice, CoursePriceAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Reservation, ReservationAdmin)