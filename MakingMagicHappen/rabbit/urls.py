from django.contrib import admin

from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
app_name = 'rabbit'

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name='rabbit/home.html'), name='home'),
    url(r'^login/$', auth_views.LoginView, {'template_name': 'rabbit/login.html'}, name='login'),
    url(r'^adopt/$', TemplateView.as_view(template_name='rabbit/adopt.html'), name='adopt'),
    url(r'^contact/$', TemplateView.as_view(template_name='rabbit/contact.html'), name='contact'),
    url(r'^rabbits/$', TemplateView.as_view(template_name='rabbit/rabbits.html'), name='rabbits'),
    #url(r'^guinea-pigs/$', TemplateView.as_view(template_name='rabbit/guinea-pigs.html'), name='guinea-pigs'),
    #url(r'^care-info/$', TemplateView.as_view(template_name='rabbit/care-info.html'), name='care-info'),
    url(r'^calendar/$', TemplateView.as_view(template_name='rabbit/calendar.html'), name='calendar'),
    url(r'^register/$', TemplateView.as_view(template_name='rabbit/register.html'), name='register'),
]

