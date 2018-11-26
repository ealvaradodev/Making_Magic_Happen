from django.shortcuts import render_to_response, render, redirect
from django.views import generic
from django.contrib.auth.models import User
from .forms import EmailServiceForm
from .models import rabbitProfile
from django.views.generic import FormView, TemplateView
from django.http import JsonResponse, HttpResponseRedirect
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
# from .forms import newUserForm

# Create your views here.
def home(request):
    return render_to_response('rabbit/home.html')

def login(request):
    return render(request,'rabbit/login.html')

def calendar(request):
    return render(request, 'rabbit/calendar.html')

def about(request):
    return render(request, 'rabbit/aboutUs.html')

class rabbit_views(generic.ListView):
    template_name='rabbit/rabbits.html'
    context_object_name = 'all_rabbit_list'
    queryset = rabbitProfile.objects.all()

    # def get_queryset(self):
    #     all_rabbit_data = rabbitProfile.objects.all()
    #     return all_rabbit_data
    
    # def get_context_data(self, **kwargs):
    #     context = super(rabbit_views, self).get_context_data(**kwargs)
    #     return context


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



# def register(request):
#     form = newUserForm()
#     if request.method == 'POST':
#         form = newUserForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             newUser = User(**form.cleaned_data)
#             newUser.save()
#         else:
#             print(form.errors)
#     context = {
#         "form" : form
#     }
#     return render(request, 'rabbit/register.html', {'form': form})
