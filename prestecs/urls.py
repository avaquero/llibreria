from django.conf.urls import patterns, url
from prestecs import views 

urlpatterns = patterns('',
    url(r'^$', views.llistatPrestecs, name='llistatPrestecs'),
    url(r'^$', views.llistatSolicituds, name='llistatSolicituds'),
    url(r'^nouPrestec/$', views.nouPrestec, name='nouPrestec'),
    url(r'^editarPrestec/(?P<idPrestec>\d+)$',views.nouPrestec, name='edita_prestec'),
    url(r'^editarSolicitud/(?P<idSolicitud>\d+)$',views.nouPrestec, name='edita_solicitud'),
    url(r'^novaSolicitud/$', views.solicitudPrestec, name='novaSolicitud'),  
)