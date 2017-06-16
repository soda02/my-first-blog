


from django.conf.urls import url
from . import views

urlpatterns = [
	 url(r'^$', views.post_list, name='post_list'),     # post_list 라는 이름의  view가  ^$  URL에 할당
]