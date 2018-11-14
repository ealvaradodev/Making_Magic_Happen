from django.db import models
from django.conf import settings

# Create your models here.
# model for the calendar event
class calendarEvent(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event_name = models.CharField(max_length= 100, null= False)
    event_time = models.TimeField((u"event Time"), auto_now_add=True, blank=True)
    event_location = models.CharField(max_length = 1000, null= False)

