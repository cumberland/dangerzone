from django.conf.urls import patterns, include, url

from cumberland import settings
from accounts.views import InviteView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^index/$', 'accounts.views.index', name='index'),
    url(r'^roundabout/$', 'accounts.views.indexroundabout', name='roundabout'),
    # url(r'^srtk/', include('srtk.foo.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/', include('userena.urls')),
    url(r'^newsletter/', include('newsletter.urls')),
    url(r'^', include('mainsite.urls')),
    url(r'^invite/$', InviteView.as_view(), name='invite'),
    url(r'^messages/', include('userena.contrib.umessages.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

)
