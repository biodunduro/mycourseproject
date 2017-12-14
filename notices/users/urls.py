from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
# Login page
	url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
# Logout page	
	url(r'^logout/$', views.logout_view, name='logout'),
	url(r'^register/$', views.register, name='register'),

]