from django.conf.urls import patterns, url
from prestecs import views 

urlpatterns = patterns('',
    url(r'^$', views.llistatPrestecs, name='llistatPrestecs'),
    
)