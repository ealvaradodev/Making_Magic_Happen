from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
app_name = 'rabbit'

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name='rabbit/home.html'), name='home'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name = 'rabbit/login.html'), name='login'),
    url(r'^adopt/$', TemplateView.as_view(template_name='rabbit/adopt.html'), name='adopt'),
    url(r'^contact/$', TemplateView.as_view(template_name='rabbit/contact.html'), name='contact'),
    url(r'^rabbits/$', TemplateView.as_view(template_name='rabbit/rabbits.html'), name='rabbits'),
    #url(r'^guinea-pigs/$', TemplateView.as_view(template_name='rabbit/guinea-pigs.html'), name='guinea-pigs'),
    #url(r'^care-info/$', TemplateView.as_view(template_name='rabbit/care-info.html'), name='care-info'),
    url(r'^calendar/$', TemplateView.as_view(template_name='rabbit/calendar.html'), name='calendar'),
    url(r'^register/$', CreateView.as_view(template_name='rabbit/register.html',form_class=UserCreationForm, success_url='/')),
    url('post/new/', views.register, name='register'),
    url(r'^deleting/$', views.usernameList, name='deleting'),
    path('rabbit/userDeleting/<int:id>/', views.userDelete,name='deleteUser'),
    path('rabbit/userChanging/<int:id>/', views.changingUserInfo,name='changingUserInfo')
]

