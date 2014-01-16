from django.conf.urls import patterns, url
from llibres import views 

from llibres import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^generes/$', views.generes, name='generes'),
)