from django.db import models

# Create your models here.

BUSINESS_TYPE =(
    ("HIGH END GYM","HIGH END"),
    ("BUDGET GYM","BUDGET GYM"),
    ("BOUTIQUE STUDIO","BOUTIQUE STUDIO"),
    ("MARTIAL ARTS","MARTIAL ARTS"),
    ("OTHER","OTHER"),

)

class Register(models.Model):
    event = models.CharField(max_length=50,null=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    address = models.TextField(max_length=100, null=True)

    def __str__(self):
        return self.event

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

