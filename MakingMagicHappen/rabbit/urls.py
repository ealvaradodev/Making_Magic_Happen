from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
app_name = 'rabbit'

urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='rabbit/home.html'), name='home'),
    url(r'^login/$', LoginView.as_view(template_name = 'rabbit/login.html'), name='login'),
    url(r'^adopt/$', TemplateView.as_view(template_name='rabbit/adopt.html'), name='adopt'),
    url(r'^contact/$', TemplateView.as_view(template_name='rabbit/contact.html'), name='contact'),
    url(r'^calendar/$', TemplateView.as_view(template_name='rabbit/calendar.html'), name='calendar'),
]

