from django.conf.urls import patterns, include, url
from mmd.views import welcome, make , result
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', welcome),
    url(r'^make/$', make),
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '/home/bilyan/ilw/pizza-for-students/html/'}), #this is to server static files
    url(r'^result/$',result),
    # url(r'^mmd/', include('mmd.foo.urls')),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
