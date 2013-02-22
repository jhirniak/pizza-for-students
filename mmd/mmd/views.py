from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader, RequestContext
from django.http import HttpResponseRedirect
from django import forms
import data_engine.user
import data_engine.query
import ast

import random
# empty file for importing
# __init__.py
import json

def welcome(request):
    csrfContext = RequestContext(request)
    print type (csrfContext)
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
    dist = request.POST['dist']

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
    u = data_engine.user.User(dict_of_features,age) # this is the User object composed of the form filled out, updated
    print u.profile
    print "this is facebook stuff"
    print facebook
    print type(facebook)
    dict_facebook = {}
    print " asd.literal ... = " + ast.literal_eval(facebook).keys()[0]
    if (ast.literal_eval(facebook).keys()[0]!="error"):
        print "ewala"
        #print len(data_engine.user.preferences_from_facebook(facebook))
        dict_facebook =  data_engine.user.preferences_from_facebook(facebook)

    print "dist : " + str(dist)
    print "dict_facebook "
    print dict_facebook

    # if we got data  from facebook
    final_dict = {}
    if dict_facebook: # if not empty
        #d = {key : (int(value1) + int(value2))/2 for (key, value1) in u.profile , (key, value2) in dict_facebook }
        for x in u.profile.keys():
            final_dict[x] = (u.profile[x] + dict_facebook[x])//2

        print "dict_facebook"
    else :
        final_dict = u.profile
    print "print final_dict" + str(final_dict)
    final_user = data_engine.user.User(final_dict,age)
    data =  data_engine.query.any_2_dict(data_engine.query.get_top_10(final_user))
    
    rc = RequestContext(request, {'data' : data } )
    return render_to_response('result.html',rc)



def result(request):
    print "results of response"
    rc = RequestContext(request, { 'foo' : request.POST  } )
    return render_to_response('result.html',rc)
