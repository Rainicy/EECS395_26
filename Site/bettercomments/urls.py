from django.conf.urls import patterns, include, url
from bettercomments import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^contact.html', 'bettercomments.views.contact', name='contact'),
    url(r'^about.html', 'bettercomments.views.about', name='about'),
    url(r'^tryrefine.html', 'bettercomments.views.tryrefine', name='tryrefine'),
    url(r'^tryrefineresults.html', 'bettercomments.views.tryrefineresults', name='tryrefineresults'),
    url(r'^index.html', 'bettercomments.views.home', name='home'),
    url(r'^test.html', 'bettercomments.views.test', name='test'),
    url(r'^comments.html', 'bettercomments.views.comments', name='comments'),
    url(r'^$', 'bettercomments.views.home', name='home'),
    # url(r'^bettercomments/', include('bettercomments.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
        (r'^static/(?P<url>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT}),
        )
