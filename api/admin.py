from django.contrib import admin
from .models import *


class RoomAdmin(admin.ModelAdmin):
    list_display = ['location', 'title', 'type', 'contact', 'is_booked']


class RoomPriceAdmin(admin.ModelAdmin):
    list_display = ['room', 'price']


class SampleDataAdmin(admin.ModelAdmin):
    list_display = ['city', 'sample_img']


class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'city', 'partner', 'room_name', 'room_detail', 'room_hash', 'room_img1', 'room_img2', 'room_img3',
        'meal_name1', 'meal_detail1', 'meal_hash1', 'meal_img1', 'meal_name2', 'meal_detail2', 'meal_hash2', 'meal_img2',
        'meal_name3', 'meal_detail3', 'meal_hash3', 'meal_img3', 'meal_name4', 'meal_detail4', 'meal_hash4', 'meal_img4',
        'meal_name5', 'meal_detail5', 'meal_hash5', 'meal_img5', 'meal_name6', 'meal_detail6', 'meal_hash6', 'meal_img6',
        'act_name1', 'act_detail1', 'act_hash1', 'act_img1', 'act_name2', 'act_detail2', 'act_hash2', 'act_img2',
        'act_name3', 'act_detail3', 'act_hash3', 'act_img3', 'result_img'
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
