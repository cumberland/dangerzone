from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'builder.views.logout_page'),	
    url(r'^main/$', 'builder.views.main'),
    url(r'^form/$', 'builder.views.form'),
    url(r'^variable/$', 'builder.views.variable'),

    url(r'^activeproject/$', 'builder.views.activeproject'),
    url(r'^activeform/$', 'builder.views.activeform'),
    url(r'^addoption/$', 'builder.views.addoption'),
    url(r'^currentoptions/$', 'builder.views.currentoptions'),
    url(r'^deleteoption/$', 'builder.views.deleteoption'),
    url(r'^deletevariable/$', 'builder.views.deletevariable'),
    url(r'^variableorder/$', 'builder.views.variableorder'),


    url(r'^project/$', 'builder.views.project'),
    url(r'^xhr_test/$', 'builder.views.xhr_test'),
    url(r'^activevar/$', 'builder.views.activevar'),
    url(r'^varsummary/$', 'builder.views.varsummary'),
    url(r'^base/$', 'builder.views.login_main_page'),
    url(r'^testprint/$', 'builder.views.testprint'),


	)