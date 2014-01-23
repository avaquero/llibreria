from django.conf.urls import patterns, url
from llibres import views 

from llibres import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^llistatGeneres/$', views.llistatGeneres, name='llistatGeneres'),
    url(r'^fitxaLlibre/(?P<idLlibre>\d+)$', views.fitxaLlibre, name='fitxaLlibre'),
    url(r'^nouGenere/$', views.entradaGeneres, name='nouGenere'),
    url(r'^editarGenere/(?P<idGenere>\d+)$', views.entradaGeneres, name='editarGenere'),
    url(r'^nouLlibre/$', views.entradaLlibre, name='nouLlibre'),
    url(r'^editarLlibre/(?P<idLlibre>\d+)$', views.entradaLlibre, name='editarLlibre'),
)