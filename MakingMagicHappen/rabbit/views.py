from django.shortcuts import render_to_response, render, redirect
from django.views import generic
from django.contrib.auth.models import User
from .forms import EmailServiceForm, newUserForm, changingUserInfoForm, rabbitSubmissionForm
from .models import rabbitProfile
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
        return redirect('/post/new/')
    context = {
        "form" : form
    }
    return render(request, 'rabbit/register.html', context)

def changingUserInfo(request, id):
    user = User.objects.get(id=id)
    form = changingUserInfoForm(request.POST or None, initial={
        'username' : user.username,
        'password' : user.password,
        'email'    : user.email,
        'first_name' : user.first_name,
        'last_name' : user.last_name,
        'is_superuser' : user.is_superuser
    })
    if form.is_valid():
        user = User(id = id, **form.cleaned_data)
        user.save()
        return redirect("/post/new/")
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
        return redirect('/post/new/')
    context = {
        "user": user
    }
    return render(request,'rabbit/deleteUser.html',context)

def about(request):
    return render(request, 'rabbit/aboutUs.html')

class rabbit_views(generic.ListView):
    template_name='rabbit/rabbits.html'
    context_object_name = 'all_rabbit_list'
    queryset = rabbitProfile.objects.all()

def eachRabbit(request,id):
    rabbit = rabbitProfile.objects.get(id = id)
    if request.method == "POST":
        return redirect('/post/new/')
    context ={
        'rabbit' : rabbit
    }
    return render(request, 'rabbit/bunnyprofile.html', context)
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


def rabbitSubmission(request):
    form = rabbitSubmissionForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        rabbit = rabbitProfile(**form.cleaned_data)
        rabbit.save()
        return redirect('./')
    context = {
        "form" : form
    }
    return render(request, 'rabbit/rabbit_submission.html', context)   