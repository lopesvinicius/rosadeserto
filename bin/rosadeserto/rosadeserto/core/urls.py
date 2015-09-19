from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('rosadeserto.core.views',
    url(r'^$', 'home', name='home'),
    url(r'^contato/$', 'contact', name='contact'),
)
