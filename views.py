from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from profiles.models import Profile
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth import authenticate, models, login, logout
from events.models import Event

def home(request):
    return render_to_response('home.html')

def login(request):
    if 'user' in request.GET and 'pwd' in request.GET:
        try:
         loginUser = Profile.objects.get(name=request.GET['user'])
        except:
         return HttpResponse('No Such Username')
        password = loginUser.password
        if password == request.GET['pwd']:
           name=request.GET['user']
           return HttpResponseRedirect('/private_page/?user=%s' % name)
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

def private_page(request):
    user=request.GET['user']
    loginUser = Profile.objects.get(name=user)
    wants_css = loginUser.want_css
    css_list = Profile.objects.filter(have_css=True)
    if loginUser.design:
      event_list = Event.objects.filter(design=True)
    else:
      event_list = []
    return render_to_response('private_page.html', {'user': user, 'wants_css': wants_css, 'css_list': css_list, 'event_list': event_list})

