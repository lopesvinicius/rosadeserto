from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^entrar/$', 'django.contrib.auth.views.login' ,
    {'template_name': 'accounts/login.html'}, name='login'),

    url(r'^sair/$', 'django.contrib.auth.views.logout',
    {'next_page': 'core:home'}, name='logout'),
   
    url(r'^cadastre-se/$', 'rosadeserto.accounts.views.register',
    name='register'),

    url(r'^confirmar-nova-senha/(?P<key>\w+)/$',
     'rosadeserto.accounts.views.password_reset_confirm',
    name='password_reset_confirm'),

    url(r'^nova-senha/$', 'rosadeserto.accounts.views.password_reset',
    name='password_reset'),

     url(r'^$', 'rosadeserto.accounts.views.dashboard',
    name='dashboard'),

    url(r'^editar/$', 'rosadeserto.accounts.views.edit',
    name='edit'),

    url(r'^editar-senha/$', 'rosadeserto.accounts.views.edit_password',
    name='edit_password'),


)
