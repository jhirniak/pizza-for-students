from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader, RequestContext
from django.http import HttpResponseRedirect
from django import forms
import data_engine.user

import random
# empty file for importing
# __init__.py
import json

def welcome(request):
    csrfContext = RequestContext(request)
    return render_to_response('index.html',csrfContext)
def make(request):
    age = request.POST['age']
    sport = request.POST['sport']
    brave = request.POST['brave']
    travel = request.POST['travel']
    friendly = request.POST['friendly']
    exploration = request.POST['exploration']
    nature = request.POST['nature']
    learning = request.POST['learning']
    facebook = request.POST['facebook'] # this is the JSON string returned by lubo
    geoLat = request.POST['geoLat']
    geoLong = request.POST['geoLong']
    print " we start "
    print "debug1"
    print facebook
    #facebook_likes = json.loads(facebook)
    #print facebook_likes
    # facebook_likes is a dictionary
    print "debug2"
    dict_of_features = {"sport": int(sport), "brave": int(brave),"travel": int(travel),"friendly": int(friendly),"exploration": int(exploration),"nature": int(nature),"learning": int(learning) }

    for x,k in dict_of_features.iteritems():
        print x + ' ' + str(k) + ' of type ' + str(type(k))
    print type(dict_of_features)
    # insert other stuff
    #print facebook_likes
    print "geo stuff"
    print "lat : " + str(geoLat) + " | long :" + str(geoLong)
    print "Jaroslaw's magic : "
    #u = data_engine.user.User(dict_of_features,age) # this is the User object composed of the form filled out, updated 
    print u.profile
    dict_facebook =  data_engine.user.preferences_from_facebook(facebook)
    
    return HttpResponseRedirect('../') # redirects
