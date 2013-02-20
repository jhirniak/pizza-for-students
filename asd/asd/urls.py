from django.conf import settings
from django.conf.urls.defaults import *
from asd.view import current_datetime, welcome # import serve

urlpatterns = patterns('',
                       (r'^time/$', current_datetime),
                       (r'^$',welcome),
                       (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/bilyan/ilw/pizza-for-students/asd/static'}),              


    )
