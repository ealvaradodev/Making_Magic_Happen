from django import forms
#Enter Your Name
#Enter email address
#Enter your Subject
#Message
class EmailServiceForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
