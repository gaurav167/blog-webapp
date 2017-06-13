from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$' ,views.index ,name = 'posts'),
	url(r'^(?P<pk>\d+)/$' ,views.page_by_num, name = 'page_by_num'),
	url(r'^(?P<category>)\w+$' ,views.page_by_name, name = 'page_by_name'),
	url(r'^(?P<num>\d+)/like/$' ,views.liked ,name='likePost'),
	url(r'^(?P<num>\d+)/dislike/$' ,views.disliked ,name='dislikePost'),
]