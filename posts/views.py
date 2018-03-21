from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def submit_blog(request):
	if request.method == "POST":
		try:
			try:
				author = request.POST.get('author')
				title = request.POST.get('title')
				subtitle = request.POST.get('subtitle')
				text = request.POST.get('text')
				categories = request.POST.get('category').lower()
				try:
					image = request.FILES['image']
				except:
					image = None
			except:
				return render(request,'message.html', {'message':'Invalid data'})
			try:
				user = User.objects.get(username=author)
			except:
				return render(request,'message.html', {'message':'No user.'})
			try:
				categ, created = Category.objects.get_or_create(name=categories)
				if created:
					categ = Category.objects.get(name=categories)
			except:
				return render(request,'message.html', {'message':"Couldn't. create category object."})					
			try:
				data={
				'author':user,
				'title':title,
				'subtitle':subtitle,
				'text':text,
				}
				new_post = Post(**data)
				new_post.publish()
				categ.assos_post.add(new_post)
				return render(request,'message.html', {'message':'Successfully posted.'})
			except:
				return render(request,'message.html', {'message':"Couldn't Post. Try again Later."})
		except:
			return render(request,'message.html', {'message':"Well, you broke what you shouldn't have. Let me call your mom."})
	else:
		return render(request,'message.html', {'message':'What are you doing bruh?. Just go and fill the form.'})


def delete_post(request,id):
	if request.method == 'DELETE':
		try:
			post = Post.objects.get(id=id)
		except:
			return render(request,'message.html', {'message':"Couldn't find the post."})
		try:
			post.delete()
			return render(request,'message.html', {'message':"Successfully deleted."})
		except:
			return render(request,'message.html', {'message':"Couldn't delete the post at the moment. Please try again later."})
	else:
		return render(request,'message.html', {'message':"Nah bro! That's not how you do it. Go back and do it the way others do, you piece of a hacker!"})


def index(request):
	posts = Post.objects.order_by('-published_date')
	return render(request,'posts/all_post.html',{'posts' : posts, 'name' : 'All Posts'})

def page_by_num(request,pk):
	posts = get_object_or_404(Post, pk=pk)
	return render(request,'posts/post.html',{'post' : posts, 'name' : posts.title})

def page_by_name(request,category):
	# posts = get_object_or_404(Post, category in categories)
	try:
		categ = Category.objects.get(name=category)
	except:
		return render(request,'message.html', {'message':"No category found by the name {}.".format(category)})
	posts = categ.assos_post.all()
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


# Category Views

def submit_category(request):
	if request.method == "POST":
		try:
			name = request.POST.get('category').lower()
		except:
			return render(request,'message.html', {'message':"Invalid data."})
		try:
			categ = Category.objects.get(name=name)
			return render(request,'message.html', {'message':"Category {} already exists.".format(name)})
		except:
			try:
				categ = Category.objects.create(name=name)
			except:
				return render(request,'message.html', {'message':"Couldn't create this category at the moment. Please try again later. Seeya!"})
			else:
				return render(request,'message.html', {'message':"Successfully created the category."})
	else:
		return render(request,'message.html', {'message':"Na Na Na! I will not accept this. Just fill the freaking form, will ya?"})


def all_categs(request):
	if request.method == "GET":
		try:
			categories = Category.objects.order_by('name')
		except:
			if request.is_ajax():
				return JsonResponse({'status':'failed','message':'No categories'})
			else:
				return render(request,'message.html', {'message':"No category."})
		if request.is_ajax():
			data = serializers.serialize('json', categories)
			return JsonResponse(data, safe=False)
		else:
			return render(request,'list.html', {'message':"All Categories."})
	else:
		if request.is_ajax():
			return JsonResponse({'error':'Only available via GET.','status_code':'400'})
		else:
			return render(request,'message.html', {'message':"Hmm! Search through your browser."})



@csrf_exempt
def category_respond(request,name,action):
	if request.method == "PUT":
		try:
			categ = Category.objects.get(name=name.lower())
		except:
			return JsonResponse({'error':'Not Found','status_code':'404'})
		try:
			action = action.lower()
			if action == 'like':
				categ.likes += 1
			elif action == 'dislike':
				categ.dislikes += 1
			categ.save()
			return JsonResponse({"status":"success"})
		except:
			return JsonResponse({'status':'failed','message':'None'})
	else:
		return JsonResponse({'error':'Only available via PUT.','status_code':'400'})


@csrf_exempt
def delete_categ(request,id):
	if request.method == 'DELETE':
		try:
			categ = Category.objects.get(pk=id)
		except:
			return JsonResponse({'status':'failed','message':'Category does not exist'})
		try:
			categ.delete()
			return JsonResponse({'status':'success'})
		except:
			return JsonResponse({'status':'failed','message':'Cannot delete category at the moment.'})
	else:
		return JsonResponse({'error':'Only available via DELETE.','status_code':'400'})
