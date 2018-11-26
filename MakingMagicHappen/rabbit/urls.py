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
    url(r'^login/$', auth_views.LoginView.as_view(template_name = 'rabbit/login.html'), name='login'),
    url(r'^adopt/$', TemplateView.as_view(template_name='rabbit/adopt.html'), name='adopt'),
    # url(r'^contact/$', TemplateView.as_view(template_name='rabbit/contact.html'), name='contact'),
    url(r'^rabbits/$', TemplateView.as_view(template_name='rabbit/rabbits.html'), name='rabbits'),
    url(r'^guinea-pigs/$', TemplateView.as_view(template_name='rabbit/guineapigs.html'), name='guineapigs'),
    #url(r'^care-info/$', TemplateView.as_view(template_name='rabbit/care-info.html'), name='care-info'),
    url(r'^donate/$', TemplateView.as_view(template_name='rabbit/donate.html'), name='donate'),
    url(r'^calendar/$', TemplateView.as_view(template_name='rabbit/calendar.html'), name='calendar'),
    url(r'^deleting/$', views.usernameList, name='deleting'),
    path('rabbit/userDeleting/<int:id>/', views.userDelete,name='deleteUser'),
    path('rabbit/userChanging/<int:id>/', views.changingUserInfo,name='changingUserInfo'),
    #url(r'^link/$', TemplateView.as_view(template_name='http://www.bunnyhugga.com/a-to-z/rabbit-behaviour/companionship.html'), name='link'),
    url(r'^register/$', CreateView.as_view(template_name='rabbit/register.html',form_class=UserCreationForm, success_url='/'),name='register'),
    url('post/new/', views.register, name='register'),
    path('contact/', views.emailService, name='contact'),
]

