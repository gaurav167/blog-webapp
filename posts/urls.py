from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'post/$' ,views.index ,name = 'posts'),
	url(r'post/(?P<pk>\d+)/$' ,views.page_by_num, name = 'page_by_num'),
	url(r'post/submit/$', views.submit_blog, name='submit_blog'),
	url(r'post/delete/(?P<id>\d+)/$', views.delete_post, name='delete_post'),
	url(r'post/(?P<category>\w+)/$' ,views.page_by_name, name = 'page_by_name'),
	url(r'post/(?P<num>\d+)/like/$' ,views.liked ,name='likePost'),
	url(r'post/(?P<num>\d+)/dislike/$' ,views.disliked ,name='dislikePost'),

	url(r'category/$', views.all_categs, name='all_categs'),
	url(r'category/submit/$', views.submit_category, name='submit_category'),
	url(r'category/delete/(?P<id>\d+)/$', views.delete_categ, name='delete_categ'),

	url(r'comment/submit/$', views.comment, name='comment'),
	url(r'comment/delete/(?P<id>\d+)/$', views.delete_comment, name='delete_comment'),

]