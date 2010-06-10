from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.conf import settings

urlpatterns = patterns('',

    # The Django admin
    (r'^admin/', include(admin.site.urls)),

    # The `polls` app
    (r'^polls/$', 'polls.views.index'),
    (r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
    (r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
    (r'^polls/(?P<poll_id>\d+)/data.xml$', 'polls.views.data'),

    # Static media
    (r'^crossdomain.xml$', 'polls.views.crossdomain'),
    (r'^local-media/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': settings.STATIC_DOC_ROOT }),

)
