from django.conf.urls import patterns, url

from roomcontrol import views

urlpatterns = patterns('',
    url(r'^$', views.main, name='main'),
    url(r'^submit$', views.submit, name='submit'),
    url(r'^retrieve$', views.retrieve, name='retrieve')
)