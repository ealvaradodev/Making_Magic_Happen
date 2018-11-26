from django import forms
from django.contrib.auth.models import User 
#Enter Your Name
#Enter email address
#Enter your Subject
#Message
class EmailServiceForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

class newUserForm(forms.Form): 
    username = forms.CharField(max_length = 150) 
    password = forms.CharField(max_length = 128) 
    email = forms.EmailField(max_length = 254) 
    first_name = forms.CharField(max_length = 30) 
    last_name = forms.CharField(max_length = 150)

class submissionForm(forms.Form):
    bunnysize = [('Small', 'Medium', 'Large')]

    rabbitname = forms.CharField(label = 'Rabbit_Name', max_length=100)
    breed = forms.CharField(label = 'Breed', max_length=150)
    gender = forms.CharField(label = 'Gender', max_length=8)
    age = forms.CharField(label = 'Age', max_length=8)
    size = forms.CharField(label = 'Size', widget = forms.Select(choices = bunnysize))
    additionalinfo = forms.TextInput()
    picture = forms.ImageField()


    
