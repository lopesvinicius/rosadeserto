from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^', include('rosadeserto.core.urls', namespace='core')),
    url(r'^conta/', include('rosadeserto.accounts.urls', namespace='accounts')),
    url(r'^cursos/', include('rosadeserto.courses.urls', namespace='courses')),
    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
	urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)