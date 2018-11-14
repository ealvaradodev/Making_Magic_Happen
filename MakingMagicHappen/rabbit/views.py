from django.shortcuts import render_to_response, render
from django.views import generic
from django.contrib.auth.models import User
from django.views.generic import FormView, TemplateView


# Create your views here.
def home(request):
    return render_to_response('rabbit/home.html')

def login(request):
    return render(request,'rabbit/login.html')

def calendar(request):
    return render(request, 'rabbit/calendar.html')