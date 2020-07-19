from django.db import models
from django.conf import settings
from .locations import LOCATION_CHOICE
from .partner import PARTNER_CHOICE


class Rooms(models.Model):
    def __str__(self):
        return self.title

    location = models.CharField(max_length=30, choices=LOCATION_CHOICE)
    title = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=PARTNER_CHOICE)
    contact = models.BigIntegerField(null=True)
    is_booked = models.BooleanField(default=False)


class RoomPrice(models.Model):
    def __str__(self):
        return str(self.price)

    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    price = models.BigIntegerField(null=False, default=0)


class SampleData(models.Model):
    def __str__(self):
        return self.keyword

    keyword = models.CharField(max_length=20, choices=LOCATION_CHOICE, null=True)
    sample_img = models.ImageField(blank=True)


class Course(models.Model):
    def __str__(self):
        return self.city

    city = models.CharField(max_length=10, choices=LOCATION_CHOICE)
    partner = models.CharField(max_length=10, choices=PARTNER_CHOICE)
    room_name = models.CharField(max_length=20, null=True)
    room_detail = models.CharField(max_length=70)
    room_hash = models.CharField(max_length=50)
    room_price = models.BigIntegerField(null=True)
    room_img1 = models.ImageField(blank=True)
    room_img2 = models.ImageField(blank=True)
    room_img3 = models.ImageField(blank=True)

    meal_name1 = models.CharField(max_length=20)
    meal_detail1 = models.CharField(max_length=70)
    meal_hash1 = models.CharField(max_length=50)
    meal_price1 = models.CharField(max_length=50, null=True)
    meal_img1 = models.ImageField(blank=True)

    meal_name2 = models.CharField(max_length=20)
    meal_detail2 = models.CharField(max_length=70)
    meal_hash2 = models.CharField(max_length=50)
    meal_price2 = models.CharField(max_length=50, null=True)
    meal_img2 = models.ImageField(blank=True)

    meal_name3 = models.CharField(max_length=20)
    meal_detail3 = models.CharField(max_length=70)
    meal_hash3 = models.CharField(max_length=50)
    meal_price3 = models.CharField(max_length=50, null=True)
    meal_img3 = models.ImageField(blank=True)

    meal_name4 = models.CharField(max_length=20)
    meal_detail4= models.CharField(max_length=70)
    meal_hash4 = models.CharField(max_length=50)
    meal_price4 = models.CharField(max_length=50, null=True)
    meal_img4 = models.ImageField(blank=True)

    meal_name5 = models.CharField(max_length=20)
    meal_detail5 = models.CharField(max_length=70)
    meal_hash5 = models.CharField(max_length=50)
    meal_price5 = models.CharField(max_length=50, null=True)
    meal_img5 = models.ImageField(blank=True)

    meal_name6 = models.CharField(max_length=20)
    meal_detail6 = models.CharField(max_length=70)
    meal_hash6 = models.CharField(max_length=50)
    meal_price6 = models.CharField(max_length=50, null=True)
    meal_img6 = models.ImageField(blank=True)

    act_name1 = models.CharField(blank=True, max_length=20)
    act_detail1 = models.CharField(blank=True, max_length=70)
    act_hash1 = models.CharField(blank=True, max_length=50)
    act_price1 = models.BigIntegerField(null=True)
    act_img1 = models.ImageField(blank=True)

    act_name2 = models.CharField(blank=True, max_length=20)
    act_detail2 = models.CharField(blank=True, max_length=70)
    act_hash2 = models.CharField(blank=True, max_length=50)
    act_price2 = models.BigIntegerField(null=True)
    act_img2 = models.ImageField(blank=True)

    act_name3 = models.CharField(blank=True, max_length=20)
    act_detail3 = models.CharField(blank=True, max_length=70)
    act_hash3 = models.CharField(blank=True, max_length=50)
    act_price3 = models.BigIntegerField(null=True)
    act_img3 = models.ImageField(blank=True)
    
    sum = models.BigIntegerField(null=True)
    result_img = models.ImageField(blank=True)


class CoursePrice(models.Model):
    def __str__(self):
        return str(self.activity)

    destination = models.ForeignKey(Course, on_delete=models.CASCADE)
    activity = models.BigIntegerField(null=True)


class Payment(models.Model):
    def __str__(self):
        return str(int(self.room_price.price) + int(self.activity_price.activity) + 5000)

    room_price = models.ForeignKey(RoomPrice, null=True, blank=True, max_length=30, on_delete=models.CASCADE)
    activity_price = models.ForeignKey(CoursePrice, max_length=30, on_delete=models.CASCADE)


class Reservation(models.Model):
    def __str__(self):
        return self.username

    username = models.CharField(max_length=20, null=False)
    phone = models.BigIntegerField(null=False)
    email = models.CharField(max_length=40, null=False)
    res_course = models.ForeignKey(Course, max_length=30, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    pay = models.ForeignKey(Payment, on_delete=models.CASCADE)
    succeed_at = models.DateTimeField(auto_now_add=True)
