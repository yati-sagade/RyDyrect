from django.conf.urls.defaults import *
import views
handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^$', views.home ),
    (r'^toggle/$', views.toggle_status),
    (r'^update/$', views.update_ip),
    (r'^logout/$', views.logout),
    (r'^people/', include('people.urls')),
    (r'^about/$', views.about),
)
