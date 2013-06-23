from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'core.views.home'),
    url(r'^analyze/$', 'core.views.analyze'),
    url(r'^admin/', include(admin.site.urls)),
)
