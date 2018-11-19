from django.shortcuts import render_to_response, render
from django.views import generic
from django.contrib.auth.models import User
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.views import generic

from .forms import modelUser

# Create your views here.
def home(request):
    return render_to_response('rabbit/home.html')

def login(request):
    return render(request,'rabbit/login.html')

def calendar(request):
    return render(request, 'rabbit/calendar.html')

def register(request):
    form = modelUser(request)
    context = {
        "form" : form
    }
    return render(request, 'rabbit/register.html', context)
"""
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    """