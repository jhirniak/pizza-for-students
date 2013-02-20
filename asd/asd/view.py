from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def welcome(request):
    #t = get_template('index_template.html') # gets the template named as the arg in the folder specified in settings.py
    #html=t.render(Context({'name' : 'Bilyan, maika ti shte eba tapo DJango shibano'}))
    # the ine bellow combines the lines above
    name = "BILYAAAANNANANAOOHOHOHOH"
    return render_to_response('index_template.html',locals())
