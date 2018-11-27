from django.db import models
from django.conf import settings

# Create your models here.
# model for the calendar event
class calendarEvent(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event_name = models.CharField(max_length= 100, null= False)
    event_time = models.TimeField((u"event Time"), auto_now_add=True, blank=True)
    event_location = models.CharField(max_length = 1000, null= False)


# model for the rabbit profile
class rabbitProfile(models.Model):
    name = models.CharField(max_length= 42, blank= False)
    Breed = models.CharField(max_length= 30)
    Gender = models.CharField(max_length= 6)
    Age = models.CharField(max_length= 10)
    Size = models.CharField(max_length= 10)
    Spayed_Neutered = models.CharField(max_length=5)
    Location = models.CharField(max_length=300, default='')
    about = models.TextField()
    profile_createdDate = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=400)

class gunieaProfile(models.Model):
    name = models.CharField(max_length= 42, blank= False)
    Breed = models.CharField(max_length= 30)
    Gender = models.CharField(max_length= 6)
    Age = models.CharField(max_length= 10)
    Size = models.CharField(max_length= 10)
    Spayed_Neutered = models.CharField(max_length=5)
    Location = models.CharField(max_length=300, default='')
    about = models.TextField()
    profile_createdDate = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=400)