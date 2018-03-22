from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth  import login as auth_login


def login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			auth_login(request, user)
			return render(request, 'users/profile.html', {'name' : user.username})
		else:
			return render(request, 'message.html', {'message' : 'Invalid User credentials.'})
	else:
		return render(request, 'users/login.html', {'name' : 'Login'})


def logout(request):
	logout(request)
