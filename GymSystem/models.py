from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

BUSINESS_TYPE =(
    ("HIGH END GYM","HIGH END"),
    ("BUDGET GYM","BUDGET GYM"),
    ("BOUTIQUE STUDIO","BOUTIQUE STUDIO"),
    ("MARTIAL ARTS","MARTIAL ARTS"),
    ("OTHER","OTHER"),

)



class Contact(models.Model):
    name = models.CharField(max_length=100);
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=60)
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Reviews(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class demo(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    business = models.CharField(max_length=20,
                                 choices=BUSINESS_TYPE,
                                 default='HIGH END GYM')
    club = models.CharField(max_length=100)
    number = models.IntegerField()
    managementSoft = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname

#Regisration
class UserDetails(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user_phone = PhoneNumberField(null=False, blank=False, unique=True, default='+91')
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    GENDER = (
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
    )
    user_gender = models.CharField(max_length=20,
                                 choices=GENDER,
                                 default=MALE)
    user_password = models.CharField(max_length=10, blank=True)


    def __str__(self):
        return str(self.user_id) if self.user_id else ''


# Course Registration
class Register(models.Model):
    event = models.CharField(max_length=50)
    u_id = models.ForeignKey(User,on_delete=models.CASCADE)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    address = models.TextField(max_length=100)

    def __str__(self):
        return self.event


class Courses(models.Model):
    cname = models.CharField(max_length=100)
    description  = models.CharField(max_length=1000)
    price = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', blank=True,null=True)
    def __str__(self):
        return self.cname

class customer(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    course_id = models.ForeignKey(Courses,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user_id) if self.user_id else ''

# Payment

class payments(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.IntegerField(null=True)

    def __str__(self):
        return self.name
class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."


class transformation(models.Model):
    day = models.CharField(max_length=50,null=True)
    excercise = models.CharField(max_length=50)
    sets = models.IntegerField()
    reps = models.IntegerField()
    tempo = models.IntegerField()
    rest = models.CharField(max_length=50)

    def __str__(self):
        return self.day
