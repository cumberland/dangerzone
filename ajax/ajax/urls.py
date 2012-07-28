from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^project/$', 'simpleform.views.project'),
    url(r'^main/$', 'simpleform.views.main'),
    url(r'^xhr_test/$', 'simpleform.views.xhr_test'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'simpleform.views.logout_page'),
    url(r'^project/$', 'simpleform.views.project'),
    url(r'^activeproject/$', 'simpleform.views.activeproject'),
    url(r'^activevar/$', 'simpleform.views.activevar'),
    url(r'^varsummary/$', 'simpleform.views.varsummary'),
    url(r'^tester/$', 'simpleform.views.tester'),
)
