from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class Destinations(models.Model):
    name=models.CharField(max_length=30)
    image=models.ImageField(upload_to='my images')
    description=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField()
    class Meta:
        db_table='dest'
    def __str__(s):
        return s.name  



class Details(models.Model) :
    title=models.CharField(max_length=50)
    Dest=models.OneToOneField(Destinations,on_delete=models.CASCADE) 
    images=models.ImageField(upload_to='destinations')
    description=models.TextField()
    day1=models.TextField()
    day2=models.TextField()
    day3=models.TextField()

    


    
    class Meta:
        db_table='details'

class Booking(models.Model):
    Firstname=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=20)
    Age=models.IntegerField()
    No_of_Persons=models.IntegerField()
    date=models.DateField()
    price=models.IntegerField(default=1)
    total=models.IntegerField(default=1)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    class Meta:
        db_table='booking'
    def __str__(s):
        return s.user  
    

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields=['Firstname','Lastname','Age','No_of_Persons','date']
    def __str__(s):
        return s.user  
    



