from django.conf.urls import url
from . import views

urlpatterns = [
	
	#Home page
	url(r'^$', views.index, name='index'),
	url(r'^publicnotices/$', views.publicnotices, name='publicnotices'),
	url(r'^publicnotices/(?P<publicnotice_id>\d+)/$', views.publicnotice, name='publicnotice'),
	url(r'^new_publicnotice/$', views.new_publicnotice, name='new_publicnotice'),
	


]