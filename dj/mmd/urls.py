from django.conf.urls.defaults import patterns, include, url
from form import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^form/$', include('form.urls')),
    # Examples:
    # url(r'^$', 'mmd.views.home', name='home'),
    # url(r'^mmd/', include('mmd.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
