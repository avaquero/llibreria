from django.conf.urls import patterns, url
from prestecs import views 

urlpatterns = patterns('',
    url(r'^$', views.llistatPrestecs, name='llistatPrestecs'),
    url(r'^llistatSolicituds$', views.llistatSolicituds, name='llistatSolicituds'),
    url(r'^nouPrestec/$', views.nouPrestec, name='nouPrestec'),
    url(r'^editarPrestec/(?P<idPrestec>\d+)$',views.nouPrestec, name='edita_prestec'),
    url(r'^editarSolicitud/(?P<idSolicitud>\d+)$',views.solicitudPrestec, name='edita_solicitud'),
    url(r'^novaSolicitud/$', views.solicitudPrestec, name='novaSolicitud'),
    url(r'^solicitar/(?P<idLlibre>\d+)$',views.novaSolicitut, name='solicitar'),
    url(r'^retornarLlibre/(?P<idLlibre>\d+)$', views.retornarLlibre, name='retornarLlibre'),
)