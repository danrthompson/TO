from django.contrib.auth import models
from django.contrib import messages
import datetime
from profiles.models import Profile

def create_event(request):
  name     = request.POST['name']
  date     = request.POST['date']
  design   = ('design' in request.POST)
  hacking  = ('hacking' in request.POST)
  social   = ('social' in request.POST)
  creator  = request.POST['creator']

  creator_profile = Profile.objects.get(name=creator)

  new_event = Event( name     = name
		   , date     = date
		   , design   = design
		   , hacking  = hacking
		   , social   = social
		   , creator  = creator_profile
		   )
  new_event.save()
  return HttpResponseRedirect('/private_page/?user=%s' % creator)
