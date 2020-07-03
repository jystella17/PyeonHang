from django.db import models
from .locations import LOCATION_CHOICE
from .partner import PARTNER_CHOICE


class Rooms(models.Model):

    def __str__(self):
        return "%s (%s)" % (self.title, self.location)

    location = models.CharField(max_length=30, choices=LOCATION_CHOICE)
    title = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=PARTNER_CHOICE)
    contact = models.BigIntegerField(null=True)
    is_booked = models.BooleanField(default=False)


class RoomPrice(models.Model):
    def __str__(self):
        return str(self.price)

    room_name = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    price = models.BigIntegerField(null=False, default=0)


class SampleData(models.Model):
    def __str__(self):
        return self.city

    city = models.CharField(max_length=20, choices=LOCATION_CHOICE)
    sample_img1 = models.ImageField(blank=True, upload_to='Pictures')
    sample_img2 = models.ImageField(blank=True, upload_to='Pictures')


class Course(models.Model):
    def __str__(self):
        return self.city

    city = models.CharField(max_length=20, choices=LOCATION_CHOICE)
    partner = models.CharField(max_length=10, choices=PARTNER_CHOICE)
    room_img1 = models.ImageField(blank=True, upload_to='Pictures')
    room_img2 = models.ImageField(blank=True, upload_to='Pictures')
    room_img3 = models.ImageField(blank=True, upload_to='Pictures')
    meal_img1 = models.ImageField(blank=True, upload_to='Pictures')
    meal_img2 = models.ImageField(blank=True, upload_to='Pictures')
    meal_img3 = models.ImageField(blank=True, upload_to='Pictures')
    meal_img4 = models.ImageField(blank=True, upload_to='Pictures')
    meal_img5 = models.ImageField(blank=True, upload_to='Pictures')
    meal_img6 = models.ImageField(blank=True, upload_to='Pictures')
    act_img1 = models.ImageField(blank=True, upload_to='Pictures')
    act_img2 = models.ImageField(blank=True, upload_to='Pictures')
    act_img3 = models.ImageField(blank=True, upload_to='Pictures')
    act_img4 = models.ImageField(blank=True, upload_to='Pictures')
    act_img5 = models.ImageField(blank=True, upload_to='Pictures')
    act_img6 = models.ImageField(blank=True, upload_to='Pictures')
    result_img = models.ImageField(blank=True, upload_to='Pictures')


class CoursePrice(models.Model):
    def __str__(self):
        return str(self.activity)

    destination = models.ForeignKey(Course, on_delete=models.CASCADE)
    activity = models.BigIntegerField(null=True)


class Payment(models.Model):
    room_price = models.ForeignKey(RoomPrice, null=True, blank=True, max_length=30, on_delete=models.CASCADE)
    activity_price = models.ForeignKey(CoursePrice, max_length=30, on_delete=models.CASCADE)

    @property
    def total_charge(self):
        return "%s" % (self.room_price + self.activity_price)
    #total = property(total_charge)


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
