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
    Spayed_Neutered= models.CharField(max_length=5)
    Location = models.CharField(max_length=300, default='')
    about = models.TextField()
    profile_createdDate = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='rabbit_image', blank= True)


#from django.contrib.auth.models import User
#from PIL import Image

# Create your models here.
#start of stuff to add images
#class Catagory(models.Model):
   # cname = models.CharField(max_length =200)
  #  purdate = models.DateTimeField('purchase-date')
 #   createdby = models.ForeignKey(User)

#class Product (models.Mode):
 #  pname = models.CharField(max_length=200)    
 #  discription = models.CharField(max_length=500)
 #  pirce = models.IntegerField()
 #  noitem = models.IntegerField()
 #   createdby = models.ForeignKey(User)
 #   cid = models.ImageField(upload_to='photo')

#class Cart(modles.Mode):
#    uid = models.ForeignKey(User)
#    pid = models.ForeignKey(Product)
#    noitem = models.IntegerField()
#   purdate = models.DateTimeField("purchase-date")
#    deldate = models.DateTimeField("delivary-date")
#end of stuff to add images
