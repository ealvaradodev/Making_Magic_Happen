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

class rabbitSubmissionForm(forms.Form):
    name = forms.CharField()
    Breed = forms.CharField()
    Gender = forms.CharField()
    Age = forms.IntegerField(max_value=100, required = False)
    Size = forms.CharField(required = False)
    Spayed_Neutered = forms.CharField(max_length=5)
    Location = forms.CharField(max_length=300)
    about = forms.CharField(widget=forms.Textarea)
    Picture = forms.ImageField()


    
