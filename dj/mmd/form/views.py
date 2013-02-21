# Create your views here.

from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponseRedirect

from django import forms

form = """<form name="input" action="submit" method="post">

<input type="submit" value="Submit"></form>"""

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
	submit = forms.Submit()

def index(request):
	return HttpResponse("Hello world!")

def form(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/form/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return HttpResponse(form)
