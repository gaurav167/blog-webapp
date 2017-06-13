from django.shortcuts import render
from django.utils import timezone
from posts.models import Post
# Create your views here.

def index(request):
	posts = Post.objects.order_by('-published_date')
	return render(request,'home/index.html',{'posts' : posts ,'name' : 'Home'})