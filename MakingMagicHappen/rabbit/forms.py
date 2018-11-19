from django import forms
from django.contrib.auth.models import User
from .models import userModel
#from .models import modelUser as md
"""
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')"""
class modelUser(forms.Form):
    username = forms.CharField(max_length = 150)
    password = forms.CharField(max_length = 128)
    email = forms.EmailField(max_length = 254)
    first_name = forms.CharField(max_length = 30)
    last_name = forms.CharField(max_length = 150)

    #class Meta:
      #  model = userModel


