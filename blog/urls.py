from django.conf.urls import url
#from . import views
from blog.views import *

urlpatterns = [
	#url(r'^$', views.post_list, name='post_list'),
	#url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	#url(r'^post/new/$', views.post_new, name='post_new'),
	#url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
 	url(r'^$', PostLV.as_view(), name='index'),
	#url(r'^$', PostLV.as_view(), name='post_list'),
	url(r'^post/$', PostLV.as_view(), name='post_list'),
	url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),
]