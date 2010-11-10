from django.conf.urls.defaults import *
from frontpage.views import *

urlpatterns = patterns('',
    (r'^$', index),
    (r'^(?P<tab>.+)$', tab_dispatcher),
)
