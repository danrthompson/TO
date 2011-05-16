from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from profiles.models import Profile
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth import authenticate, models, login, logout

def home(request):
    return render_to_response('home.html')

def login(request):
    if 'user' in request.GET and 'pwd' in request.GET:
        try:
         loginUser = Profile.objects.get(name=request.GET['user'])
        except:
         message = 'No Such Username'
        password = loginUser.password
        if password == request.GET['pwd']:
            HttpResponseRedirect('/private_page/')
        else:
           message = 'wrong pass'
    else:
	message = 'Error'
    return HttpResponse(message)

def check_auth(request):
    if 'pwd' in request.GET:
        if request.GET['pwd'] == 'special':
	    return HttpResponseRedirect('/new_profile/')
	else:
	    message = 'Wrong password'
    else:
	message = 'Error'
    return HttpResponse(message)

