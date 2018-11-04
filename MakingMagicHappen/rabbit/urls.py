from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
app_name = 'rabbit'

urlpatterns = [
	path('', views.home, name='home'),
	# path('home/', views.homeViewView.as_view()), name='home'),
]

