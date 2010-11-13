from django.conf.urls.defaults import *
from frontpage.views import *

urlpatterns = patterns('',
    (r'^$', index),
    (r'^add_user', add_user),
    (r'^(?P<tab>.+)$', tab_dispatcher),
)
