"""URLs to run the tests."""
from django.conf.urls import include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^command-interface/', include('command_interface.urls')),
]

try:
    from django.conf.urls import patterns
    urlpatterns = patterns(
        '',
        *urlpatterns
    )
except ImportError:
    pass
