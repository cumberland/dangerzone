from newage.views import MyView, HomePageView
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
    url(r'^pdftest/$', 'simpleform.views.pdf_test'),
    url(r'^article/$', 'simpleform.views.article'),
    url(r'^projectedit/$', 'simpleform.views.projectedit'),
    url(r'^selectable/', include('selectable.urls')),
    url(r'^fancy/$', 'simpleform.views.fancy'),
    url(r'^calendar/$', 'simpleform.views.calendar'),
    url(r'^addavailable/$', 'simpleform.views.addavailable'),
    url(r'^accounts/', include('userena.urls')),
    url(r'^newage/$', 'newage.views.newage'),
    url(r'^newageedit/(?P<test_id>\d+)/$', 'newage.views.newageedit'),
    url(r'^newageset/$', 'newage.views.newageset'),
    url(r'^mine/$', MyView.as_view(), name='my-view'),
    url(r'^$', HomePageView.as_view(), name='home'),
)
