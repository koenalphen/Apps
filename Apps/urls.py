from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Apps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('trackTime.urls', namespace='trackTime')),
    url(r'^trackTime/', include('trackTime.urls', namespace='trackTime')),
    url(r'^roomcontrol/', include('roomcontrol.urls', namespace='roomcontrol'))
)
