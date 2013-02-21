from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader, RequestContext
from django.http import HttpResponseRedirect
from django import forms


def welcome(request):
    csrfContext = RequestContext(request)
    return render_to_response('index.html',csrfContext)
def make(request):
    if request.POST['text'] :
        text = request.POST['text']
        print text
    print request.POST['age']
    print request.POST['sport']
    return HttpResponseRedirect('../') # redirects
