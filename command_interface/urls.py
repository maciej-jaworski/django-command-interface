"""URLs for the command_interface app."""
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.CommandInterfaceMainView.as_view(), name='command_interface_main'),
]

try:
    from django.conf.urls import patterns
    urlpatterns = patterns(
        '',
        *urlpatterns
    )
except ImportError:
    pass
