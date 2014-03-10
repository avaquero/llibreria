from django.conf.urls import patterns, url
from llibres import views 

from llibres import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^llistatGeneres/$', views.llistatGeneres, name='llistatGeneres'),
    url(r'^fitxaLlibre/(?P<idLlibre>\d+)$', views.fitxaLlibre, name='fitxaLlibre'),
    url(r'^fitxaTitol/(?P<idTitol>\d+)$', views.fitxaTitol, name='fitxaTitol'),
    #url(r'^nouGenere/$', views.entradaGeneres, name='nouGenere'),
   # url(r'^editarGenere/(?P<idGenere>\d+)$', views.entradaGeneres, name='editarGenere'),
    url(r'^nouLlibre/$', views.entradaLlibre, name='nouLlibre'),
    url(r'^nouTitol/$', views.entradaTitols, name='nouTitol'),
    url(r'^editarTitol/(?P<idTitol>\d+)$', views.entradaTitols, name='editarTitol'),
    url(r'^editarLlibre/(?P<idLlibre>\d+)$', views.entradaLlibre, name='editarLlibre'),
    url(r'^genere/(?P<idGenere>\d+)$', views.llistatTitolsDeGenere, name='titolsDeGenere'),
    url(r'^llistatTitols/$', views.llistatTitols, name='llistatTitols'),
)