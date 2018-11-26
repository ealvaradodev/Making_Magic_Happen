from django.shortcuts import render_to_response, render, redirect
from django.views import generic
from django.contrib.auth.models import User
from .forms import EmailServiceForm, newUserForm, changingUserInfoForm
from django.views.generic import FormView, TemplateView
from django.http import JsonResponse, HttpResponseRedirect
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def home(request):
    return render_to_response('rabbit/home.html')

def login(request):
    return render(request,'rabbit/login.html')

def calendar(request):
    return render(request, 'rabbit/calendar.html')
  
def register(request):
    form = newUserForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        newUser = User(**form.cleaned_data)
        newUser.save()
    context = {
        "form" : form
    }
    return render(request, 'rabbit/register.html', context)

def changingUserInfo(request, id):
    form = changingUserInfoForm(request.POST or None)
    user = User.objects.get(id=id)
    if form.is_valid():
        print(form.cleaned_data)
        if ('username' in form.cleaned_data) != '':
            newUsername = form.cleaned_data['username']
        else:
            newUsername = user.username

        if ('password' in form.cleaned_data) != '':
            newPassword = form.cleaned_data['password']
        else:
            newPassword = user.password

        if ('email' in form.cleaned_data) != '':
            print(form.cleaned_data['email'])
            newEmail = form.cleaned_data['email']
        else:
            newEmail = user.email

        if ('first_name' in form.cleaned_data) != '':
            newFirstName = form.cleaned_data['first_name']
        else:
            newFirstName = user.first_name
        
        if ('last_name' in form.cleaned_data) != '':
            newLastName = form.cleaned_data['last_name']
        else:
            newLastName = user.last_name
        user = User(
            id = id, 
            username = newUsername, 
            password = newPassword, 
            email = newEmail, 
            first_name = newFirstName, 
            last_name = newLastName,
            is_superuser = form.cleaned_data['is_superuser']
            )
        user.save()
        return redirect("../../../post/new/")
    context = {
        "changingForm" : form,
        "user" : user
    }
    return render(request, 'rabbit/changing.html', context)


def usernameList(request):
    queryset = User.objects.all()
    context = {
        "object_list" : queryset
    }
    return render(request, 'rabbit/deleting.html', context)

def userDelete(request, id):
    user = User.objects.get(id=id)
    if request.method == "POST":
        user.delete()
        return redirect('../../../post/new/')
    context = {
        "user": user
    }
    return render(request,'rabbit/deleteUser.html',context)

def about(request):
    return render(request, 'rabbit/aboutUs.html')

#Enter email address
#Enter your Subject
#Message
def emailService(request):
    if request.method == 'GET':
        form = EmailServiceForm
    else:
        form = EmailServiceForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email,['bistaaliza@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/contact')
    return render(request, "rabbit/contact.html", {'form':form})
