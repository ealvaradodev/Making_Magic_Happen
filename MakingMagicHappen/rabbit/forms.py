from django import forms
from django.contrib.auth.models import User 





class newUserForm(forms.Form): 
    username = forms.CharField(max_length = 150, required = True) 
    password = forms.CharField(max_length = 128, required = True,widget=forms.PasswordInput()) 
    email = forms.EmailField(max_length = 254, required = True) 
    first_name = forms.CharField(max_length = 30, required = False) 
    last_name = forms.CharField(max_length = 150, required = False)
    is_superuser = forms.BooleanField(required=False)

class changingUserInfoForm(forms.Form): 
    username = forms.CharField(max_length = 150, required = False) 
    password = forms.CharField(max_length = 128, required = False,widget=forms.PasswordInput())
    email = forms.EmailField(max_length = 254, required = False) 
    first_name = forms.CharField(max_length = 30, required = False) 
    last_name = forms.CharField(max_length = 150, required = False)
    is_superuser = forms.BooleanField(required=False)
#Enter Your Name
#Enter email address
#Enter your Subject
#Message
class EmailServiceForm(forms.Form):
    your_Email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

SIZE_CHOICES = [('Small','Small'),('Medium', 'Medium'),('Large','Large')]
AGE_CHOICES = [('Young','Young'),('Adult', 'Adult')]
GENDER_CHOICES = [('Male','Male'),('Female', 'Female')]
FIXED_CHOICES = [('Yes','Yes'),('No', 'No')]
ANIMAL_CHOICES = [('Rabbit','Rabbit'),('Guinea Pig', 'Guinea Pig')]

class rabbitSubmissionForm(forms.Form):

    
    animalType = forms.CharField( widget = forms.RadioSelect(choices =ANIMAL_CHOICES))
    Name = forms.CharField()
    Breed = forms.CharField()
    Gender = forms.CharField( widget = forms.RadioSelect(choices =GENDER_CHOICES))
    
    Age = forms.CharField( widget = forms.RadioSelect(choices =AGE_CHOICES))
    Size = forms.CharField( widget = forms.RadioSelect(choices =SIZE_CHOICES))#forms.CharField(required = False)
    Spayed_Neutered = forms.CharField( widget = forms.RadioSelect(choices =FIXED_CHOICES))
    Location = forms.CharField(max_length=300)
    About = forms.CharField(widget=forms.Textarea)
    # image = forms.ImageField()


    
