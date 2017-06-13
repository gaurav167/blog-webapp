from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.http import HttpResponse

# Create your views here.

def index(request):
	posts = Post.objects.order_by('-published_date')
	return render(request,'posts/all_post.html',{'posts' : posts, 'name' : 'All Posts'})

def page_by_num(request,pk):
	posts = get_object_or_404(Post, pk=pk)
	return render(request,'posts/post.html',{'post' : posts, 'name' : posts.title})

def page_by_name(request,category):
	posts = get_object_or_404(Post, category in categories)
	return render(request,'posts/post.html',{'post' : posts})

def liked(request,num):
	posts = Post.objects.filter(pk=num)
	active = request.GET.get('active')
	for post in posts:
		if active == 'false':
			post.likes += 1
		else:
			post.likes -= 1
		post.save()
	return HttpResponse(post.likes)

def disliked(request,num):
	posts = Post.objects.filter(pk=num)
	active = request.GET.get('active')
	for post in posts:
		if active == 'false':
			post.dislikes += 1
		else:
			post.dislikes -= 1
		post.save()
	return HttpResponse(post.dislikes)