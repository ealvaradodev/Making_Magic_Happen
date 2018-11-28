from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import path
from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
app_name = 'rabbit'

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name='rabbit/home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='rabbit/aboutUs.html'), name='about'),
    url(r'^volunteer/$', TemplateView.as_view(template_name='rabbit/volunteer.html'), name='volunteer'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name = 'rabbit/login.html'), name='login'),
    url(r'^adopt/$', TemplateView.as_view(template_name='rabbit/adopt.html'), name='adopt'),
    url(r'^rabbits/$', views.rabbit_views.as_view(), name='rabbits'),
    path('rabbits/bunnyprofile/<int:id>/', views.eachRabbit, name='bunnyprofile'),
    url(r'^guniea/$', views.guniea_views.as_view(), name='guniea'),
    path('guniea/gunieaprofile/<int:id>/', views.eachGuniea, name='gunieaprofile'),
    #url(r'^care-info/$', TemplateView.as_view(template_name='rabbit/care-info.html'), name='care-info'),
    url(r'^donate/$', TemplateView.as_view(template_name='rabbit/donate.html'), name='donate'),
    url(r'^calendar/$', TemplateView.as_view(template_name='rabbit/calendar.html'), name='calendar'),
    url(r'^deleting/$', login_required(views.usernameList), name='deleting'),
    url('submission/', login_required(views.submission), name='submission'),
    path('rabbit/userDeleting/<int:id>/', login_required(views.userDelete),name='deleteUser'),
    path('rabbit/userChanging/<int:id>/', login_required(views.changingUserInfo),name='changingUserInfo'),
    url('post/new/', login_required(views.register), name='register'),
    path('contact/', views.emailService, name='contact'),
    url(r'^register/$', CreateView.as_view(template_name='rabbit/register.html',form_class=UserCreationForm, success_url='/')),
    url('post/new/', views.register, name='register'),
]

