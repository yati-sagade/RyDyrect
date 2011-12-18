from django.conf.urls.defaults import *
import views

urlpatterns = patterns( '',
                       (r'^(?P<nick>[^/]*)/$', views.redir),
                       (r'^(?P<nick>[^/]*)/(?P<path_hence>.*)/$', views.redir),
                      )

