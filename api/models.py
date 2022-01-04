from django.db import models
from django.conf import settings
from .locations import LOCATION_CHOICE
from .partner import PARTNER_CHOICE


class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now_add=True)


class Rooms(models.Model):
    def __str__(self):
        return "%s (%s)" % (self.title, self.location)

    location = models.CharField(max_length=30, choices=LOCATION_CHOICE)
    title = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=PARTNER_CHOICE)
    price = models.BigIntegerField(null=False, default=0)
    contact = models.BigIntegerField(null=True)
    is_booked = models.BooleanField(default=False)


class Course(models.Model):
    def __int__(self):
        return self.id

    city = models.CharField(max_length=10, choices=LOCATION_CHOICE)
    partner = models.CharField(max_length=10, choices=PARTNER_CHOICE)
    room_name = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    room_detail = models.CharField(max_length=50)
    room_hash = models.CharField(max_length=50)
    room_img1 = models.ImageField(blank=True, upload_to='')
    room_img1 = models.ImageField(blank=True, upload_to='')
    room_img2 = models.ImageField(blank=True, upload_to='')
    room_img3 = models.ImageField(blank=True, upload_to='')

    meal_name1 = models.CharField(max_length=20)
    meal_detail1 = models.CharField(max_length=50)
    meal_hash1 = models.CharField(max_length=50)
    meal_img1 = models.ImageField(blank=True, upload_to='')

    meal_name2 = models.CharField(max_length=20)
    meal_detail2 = models.CharField(max_length=50)
    meal_hash2 = models.CharField(max_length=50)
    meal_img2 = models.ImageField(blank=True, upload_to='')

    meal_name3 = models.CharField(max_length=20)
    meal_detail3 = models.CharField(max_length=50)
    meal_hash3 = models.CharField(max_length=50)
    meal_img3 = models.ImageField(blank=True, upload_to='')

    meal_name4 = models.CharField(max_length=20)
    meal_detail4= models.CharField(max_length=50)
    meal_hash4 = models.CharField(max_length=50)
    meal_img4 = models.ImageField(blank=True, upload_to='')

    meal_name5 = models.CharField(max_length=20)
    meal_detail5 = models.CharField(max_length=50)
    meal_hash5 = models.CharField(max_length=50)
    meal_img5 = models.ImageField(blank=True, upload_to='')

    meal_name6 = models.CharField(max_length=20)
    meal_detail6 = models.CharField(max_length=50)
    meal_hash6 = models.CharField(max_length=50)
    meal_img6 = models.ImageField(blank=True, upload_to='')

    act_name1 = models.CharField(blank=True, max_length=20)
    act_detail1 = models.CharField(blank=True, max_length=50)
    act_hash1 = models.CharField(blank=True, max_length=50)
    act_img1 = models.ImageField(blank=True, upload_to='')

    act_name2 = models.CharField(blank=True, max_length=20)
    act_detail2 = models.CharField(blank=True, max_length=50)
    act_hash2 = models.CharField(blank=True, max_length=50)
    act_img2 = models.ImageField(blank=True, upload_to='')

    act_name3 = models.CharField(blank=True, max_length=20)
    act_detail3 = models.CharField(blank=True, max_length=50)
    act_hash3 = models.CharField(blank=True, max_length=50)
    act_img3 = models.ImageField(blank=True, upload_to='')

    price = models.BigIntegerField(default=0)
    result_img = models.ImageField(blank=True, upload_to='')


class Reservation(models.Model):
    def __str__(self):
        return self.username

    username = models.CharField(max_length=20, null=False)
    phone = models.BigIntegerField(null=False)
    email = models.CharField(max_length=40, null=False)
    res_course = models.ForeignKey(Course, max_length=30, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    payment = models.ForeignKey(
        Course, related_name='course_payment', on_delete=models.CASCADE, db_column='price', default=0
    )
    booked_at = models.DateTimeField(auto_now_add=True)
