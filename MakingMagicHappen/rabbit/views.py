from django.shortcuts import render_to_response, render
from django.views import generic
from django.views.generic import FormView, TemplateView


# Create your views here.
def home(request):
    return render_to_response('rabbit/home.html')

def login(request):
    return render(request,'rabbit/login.html')