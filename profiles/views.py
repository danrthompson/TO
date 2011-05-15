from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from profiles.models import Profile
from django.contrib.auth import models
from django.contrib import messages
import datetime

def new_profile(request):
    return render_to_response('new_profile.html')

def create_profile(request):
  name          = request.POST['name']
  password      = request.POST['pwd']
  email         = request.POST['email']
  design        = ('design' in request.POST)
  have_css      = ('have_css' in request.POST)
  have_php      = ('have_php' in request.POST)
  want_css      = ('want_css' in request.POST)
  want_php      = ('want_php' in request.POST)
  date_created  = datetime.datetime.now()

  new_profile = Profile( name          = name
		       , password      = password
		       , email         = email
		       , design        = design
		       , have_css      = have_css
		       , have_php      = have_php
		       , want_css      = want_css
		       , want_php      = want_php
		       , date_created  = date_created
		       )
  new_profile.save()

  return HttpResponse('yay')
