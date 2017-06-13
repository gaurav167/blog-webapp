from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,'contact/contact.html',{'name' : 'Contact Us'})

def submit(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		message = request.POST['message']

	subject = 'TOTAL BLOGGER : ' + name + ' WANTS TO CONTACT YOU.'
	send_message = email + ' SENT THIS.\n' + message
	from_email = settings.EMAIL_HOST_USER
	to_list = ['gaurav.goel167@gmail.com']
	send_mail(
    subject,
    send_message,
    from_email,
    to_list,
    fail_silently=True,
	)
	return HttpResponse('')