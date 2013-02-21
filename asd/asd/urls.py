from django.conf import settings
from django.conf.urls.defaults import *
from asd.view import current_datetime, welcome # import serve

urlpatterns = patterns('',
                       (r'^time/$', current_datetime),
                       (r'^$',welcome),
                       (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/bilyan/ilw/pizza-for-students/asd/static'}),
                       (r'^facebook/', include('django_facebook.urls')),
                       (r'^accounts/', include('django_facebook.auth_urls')), #Don't add this line if you use django registration or userena for registration and auth.


    )
