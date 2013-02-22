#coding: utf8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader, RequestContext
from django.http import HttpResponseRedirect
from django import forms
import data_engine.user
from data_engine.label_data import data
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
    print " we start "
    #facebook_test = unicode(r"""
    #{"data":[{"category":"Computers/internet website","name":"Freemake","id":"125351867496875","created_time":"2013-02-10T02:43:10+0000"},{"category":"Movie","name":"Ice Age 2","id":"106050296101643","created_time":"2013-01-29T12:15:47+0000"},{"category":"Product/service","name":"Facebook Developers","id":"19292868552","created_time":"2013-01-03T12:14:25+0000"},{"category":"Movie","name":"Pirates of the Caribbean","id":"113294925350820","created_time":"2012-12-09T23:31:02+0000"},{"category":"Movie","name":"Ice Age Movie","id":"129577537128630","created_time":"2012-12-09T23:30:59+0000"},{"category":"Tv show","name":"Tom And Jerry","id":"131583793581459","created_time":"2012-12-09T23:29:58+0000"},{"category":"Interest","name":"Java","id":"104095292959576","created_time":"2012-12-09T23:29:53+0000"},{"category":"Community","name":"Blackrock Programming Competition","id":"174215209385841","created_time":"2012-12-03T20:56:56+0000"},{"category":"University","name":"Appleton Tower","id":"98967031653","created_time":"2012-12-01T05:11:10+0000"},{"category":"Amateur sports team","name":"Glasgow University Men's Volleyball Club","id":"409495892438497","created_time":"2012-09-26T19:08:42+0000"},{"category":"Product/service","name":"BG Live Republic","id":"385540994803917","created_time":"2012-09-22T17:50:03+0000"},{"category":"Athlete","name":"Dimitar Berbatov","id":"7232253525","created_time":"2012-07-25T08:15:07+0000"},{"category":"Company","name":"Vivacom","id":"130400777004291","created_time":"2012-07-08T20:12:59+0000"},{"category":"Education","name":"Have Fun With Russian","id":"204801422899473","created_time":"2012-05-07T23:08:26+0000"},{"category":"Other","name":"Get a cat they said.... it will be fun they said!","id":"232061916895982","created_time":"2012-05-01T15:47:37+0000"},{"category":"App page","name":"Chess.com","id":"14110019570","created_time":"2012-04-27T17:38:37+0000"},{"category":"Community","name":"Edinburgh University Bulgarian Society","id":"310639142337240","created_time":"2012-04-01T19:07:45+0000"},{"category":"Other","name":"You know is true...","id":"303845736336010","created_time":"2012-02-22T15:19:30+0000"},{"category":"Community","name":"My Borovets","id":"188504251175828","created_time":"2011-12-17T11:39:13+0000"},{"category":"Travel/leisure","name":"British Airways","id":"76903425829","created_time":"2011-12-13T17:47:09+0000"},{"category":"Local business","name":"Hermit's Croft","id":"122153647857271","created_time":"2011-12-02T18:33:10+0000"},{"category":"City","name":"Edinburgh, United Kingdom","id":"115753025103602","created_time":"2011-11-06T12:03:04+0000"},{"category":"Arts/entertainment/nightlife","name":"EUSAlive","id":"153486764687595","created_time":"2011-10-25T23:30:17+0000"},{"category":"Games/toys","name":"Call of Duty: Modern Warfare 2","id":"62248718804","created_time":"2011-10-17T18:34:36+0000"},{"category":"Product/service","name":"PHP","id":"6358087478","created_time":"2011-08-28T13:41:38+0000"},{"category":"Non-profit organization","name":"GeoGebra","id":"101205123231","created_time":"2011-08-28T13:41:27+0000"},{"category":"News/media website","name":"PixelMedia.bg","id":"206358842191","created_time":"2011-08-28T13:40:56+0000"},{"category":"Local business","name":"ROCK'N'ROLLA","id":"313115914842","created_time":"2011-08-24T13:28:35+0000"},{"category":"Organization","name":"University of Edinburgh School of Informatics","id":"103758349662479","created_time":"2011-08-24T12:42:42+0000"},{"category":"Radio station","name":"Alpha Radio Bulgaria","id":"103957586364061","created_time":"2011-08-18T10:26:32+0000"},{"category":"School","name":"National High School of Mathematics and Science","id":"111882592163549","created_time":"2011-08-04T14:44:34+0000"},{"category":"School","name":"NPMG","id":"120463371298567","created_time":"2011-04-24T00:12:53+0000"},{"category":"Community","name":"Ïàðêåò ÀÍÄÈ ÎÎÄ","id":"118245221588384","created_time":"2011-04-18T09:40:53+0000"},{"category":"Product/service","name":"GoPro","id":"50043151918","created_time":"2011-03-16T06:56:19+0000"},{"category":"Musician/band","name":"UKF Drum & Bass","id":"274197690441","created_time":"2011-03-05T21:26:35+0000"},{"category":"Musician/band","name":"UKF Dubstep","id":"150212395208","created_time":"2011-01-26T16:53:48+0000"},{"category":"Outdoor gear/sporting goods","name":"XCoSports Bulgaria","id":"67902210801","created_time":"2011-01-19T11:11:45+0000"},{"category":"Athlete","name":"Àëåêñàíäðà \"Ñàíè\" Æåêîâà","id":"389308271207","created_time":"2011-01-17T20:46:36+0000"},{"category":"Interest","name":"Programming","id":"101882226520576","created_time":"2011-01-16T21:43:43+0000"},{"category":"Field of study","name":"Music","id":"112936425387489","created_time":"2011-01-16T21:43:40+0000"},{"category":"Field of study","name":"Movies","id":"106057162768533","created_time":"2011-01-16T21:43:38+0000"},{"category":"Interest","name":"Driving","id":"112132342136485","created_time":"2011-01-16T21:43:35+0000"},{"category":"Athlete","name":"Alberto Tomba","id":"107488809273907","created_time":"2011-01-16T21:38:35+0000"},{"category":"Sport","name":"Skiing","id":"103780659661402","created_time":"2011-01-13T09:01:25+0000"},{"category":"Outdoor gear/sporting goods","name":"Rossignol","id":"13712643396","created_time":"2010-12-16T20:52:04+0000"},{"category":"Product/service","name":"YouTube","id":"7270241753","created_time":"2010-11-15T20:58:44+0000"},{"category":"Media/news/publishing","name":"Sportal.bg","id":"117424930572","created_time":"2010-09-09T09:36:19+0000"},{"category":"Software","name":"MySQL","id":"7802084642","created_time":"2010-06-16T20:18:54+0000"},{"category":"Website","name":"Facebook Developers","id":"111141618921610","created_time":"2010-06-14T19:39:50+0000"},{"category":"Tv","name":"àëàìèíóò","id":"113227912035696","created_time":"2010-05-09T18:38:37+0000"},{"category":"Movie","name":"The Transporter","id":"105485349484433","created_time":"2010-05-09T18:38:36+0000"},{"category":"Attractions/things to do","name":"Bansko Winter Resort","id":"193429496939","created_time":"2010-04-24T10:50:54+0000"},{"category":"Product/service","name":"Mozilla Firefox","id":"14696440021","created_time":"2010-04-04T12:36:55+0000"},{"category":"Community","name":"-SMOKING IS UNATTRACTIVE && DISGUSTING!-","id":"124917899963","created_time":"2010-02-24T20:16:16+0000"},{"category":"Community","name":"ÍÅ ÑÅ ÑÐÀÌÓÂÀÌ ÎÒ ÐÎÄÈÒÅËÈÒÅ ÑÈ","id":"479789415509","created_time":"2010-02-12T17:24:59+0000"},{"category":"Tv show","name":"24","id":"14176232250","created_time":"2010-01-13T08:59:51+0000"},{"category":"Musician/band","name":"Pop","id":"114541715224893"}],"paging":{"next":"https://graph.facebook.com/100000015374265/likes?access_token=AAACORKyXRNEBAJBPWYSYmjiZCggPJHE1SLeUdEhYyVCGtkpjCGzOoozkJ67wUU2GHV9Xfi8HJzsgg5zR2NwNb0WTNnHBRhqE2crm3vZB1JEWZCZAQJsL&limit=5000&offset=5000&__after_id=114541715224893"}}""",'utf_8')
    print "debug1"
    print facebook
    #facebook_likes = json.loads(facebook)
    # facebook_likes is a dictionary
    print "debug2"
    dict_of_features = {"age": int(age) ,"sport": int(sport), "brave": int(brave),"travel": int(travel),"friendly": int(friendly),"exploration": int(exploration),"nature": int(nature),"learning": int(learning) }

    for x,k in dict_of_features.iteritems():
        print x + ' ' + str(k) + ' of type ' + str(type(k))
    print type(dict_of_features)
    # insert other stuff
    #print facebook_likes
    print "Jaroslaw's magic : "
    u = data_engine.user.User(dict_of_features) # this is the User object composed of the form filled out
    print u.profile
    print "magic ? "
    x = [ (u.evaluate_location(d), d.name) for d in data ]
    t = random.random() < 0.5
    x = sorted(x, key=lambda (x,y): x)[::-1][0 if t else 1:3 if t else 4]
    print x
    return HttpResponseRedirect('../') # redirects
