from django.db import models
import uuid
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.



class admin_register(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4, editable = False)
    otp = models.CharField(max_length=50)
    name_of_org = models.CharField(max_length=30, unique=True)
    year_of_foundation = models.IntegerField()
    contact_number = models.IntegerField()
    username = models.CharField(max_length= 10, unique= True)
    email = models.EmailField(unique= True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verify = models.BooleanField(default=False)
    

    

    def __str__(self):
        return "%s" % self.name_of_org


class user_attendance_monitor(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)
    contact = models.IntegerField()
    login_time = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return "%s" % self.name


class user_register(models.Model):

    Male = 'M'
    Female = 'F'
    Transgender = 'TRANS'

    gender_choices = [
        (Male, 'Male'),
        (Female, 'Female'),
        (Transgender, 'Transgender'),
    ]
    
    member_id = models.CharField(max_length= 6, null=False)
    uid = models.UUIDField(unique= True,default = uuid.uuid4, editable = False)
    name_of_org = models.ForeignKey(admin_register, on_delete=models.DO_NOTHING, null=True)
    otp = models.CharField(max_length=50)
    name = models.CharField(max_length=30, unique= True)
    gender = models.CharField(max_length=12, choices= gender_choices, default= Male)
    username = models.CharField(max_length= 10, unique= True)
    date_of_birth = models.DateField(null = True)
    contact = models.CharField(max_length=10)
    email = models.EmailField(unique= True)
    verify = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    
    
    def __str__(self):
        return "%s is User " % self.name


class user_notifications(models.Model):
    notify = models.CharField(max_length=50 )   
    person = models.TextField(max_length=50)

    def __str__(self):
        return "%s " % self.notify


class membership(models.Model):
    membership_type =  models.CharField(max_length=10)
    description = models.CharField(max_length=50)
    original_price = models.IntegerField(null = True)
    discount_percentage = models.IntegerField(null = True)
    discounted_price= models.IntegerField(null = True)
    name_of_org = models.CharField(max_length=50)

    def __str__(self):
        return "%s " % self.membership_type
    


