from django.db import models

# Create your models here.

class Registration(models.Model):
    first_name = models.CharField(max_length= 20)
    last_name = models.CharField(max_length= 20)
    email = models.CharField(max_length= 40)
    password = models.CharField(max_length= 50)
    
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    content = models.CharField(max_length=100)
    
class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

class Booking(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()

    def __str__(self):
        return f"{self.car} - {self.user_name}"
