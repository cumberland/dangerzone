from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^project/$', 'builder.views.project'),
    url(r'^main/$', 'builder.views.main'),
    url(r'^xhr_test/$', 'builder.views.xhr_test'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'builder.views.logout_page'),
    url(r'^project/$', 'builder.views.project'),
    url(r'^activeproject/$', 'builder.views.activeproject'),
    url(r'^activevar/$', 'builder.views.activevar'),
    url(r'^varsummary/$', 'builder.views.varsummary'),
    url(r'^base/$', 'builder.views.login_main_page'),
    url(r'^testprint/$', 'builder.views.testprint'),
    url(r'^addoption/$', 'builder.views.addoption'),
    url(r'^currentoptions/$', 'builder.views.currentoptions'),
    url(r'^deleteoption/$', 'builder.views.deleteoption'),
	)