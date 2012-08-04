from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^project/$', 'simpleform.views.project'),
    url(r'^main/$', 'simpleform.views.main'),
    url(r'^xhr_test/$', 'simpleform.views.xhr_test'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'simpleform.views.logout_page'),
    url(r'^project/$', 'simpleform.views.project'),
    url(r'^activeproject/$', 'simpleform.views.activeproject'),
    url(r'^activevar/$', 'simpleform.views.activevar'),
    url(r'^varsummary/$', 'simpleform.views.varsummary'),
	)