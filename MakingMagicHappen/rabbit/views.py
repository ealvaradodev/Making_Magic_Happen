from django.shortcuts import render_to_response, render
from django.views import generic
from django.contrib.auth.models import User
from django.views.generic import FormView, TemplateView
from django.http import JsonResponse, HttpResponseRedirect
from .forms import newUserForm

# Create your views here.
def home(request):
    return render_to_response('rabbit/home.html')

def login(request):
    return render(request,'rabbit/login.html')

def calendar(request):
    return render(request, 'rabbit/calendar.html')

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken' : User.objects.filter(username__isexact = username).e
    }
    return JsonResponse(data)


def register(request):
    form = newUserForm()
    if request.method == 'POST':
        form = newUserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            newUser = User(**form.cleaned_data)
            newUser.save()
        else:
            print(form.errors)
    context = {
        "form" : form
    }
    return render(request, 'rabbit/register.html', context)