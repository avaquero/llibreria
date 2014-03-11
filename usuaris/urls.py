from django.conf.urls import patterns, url
from usuaris import views 

urlpatterns = patterns('',
    url(r'^$', views.infoUsuari, name='llistatUsuaris'),
    url(r'^login$', views.entrada, name='login'),
    url(r'^logout$', views.logout_view, name='logout'),
)