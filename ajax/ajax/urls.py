from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ajax.views.home', name='home'),
    # url(r'^ajax/', include('ajax.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^start/$', 'simpleform.views.start'),
    url(r'^main/$', 'simpleform.views.main'),
    url(r'^xhr_test/$', 'simpleform.views.xhr_test'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'simpleform.views.logout_page'),
    url(r'^project/$', 'simpleform.views.project'),
)
