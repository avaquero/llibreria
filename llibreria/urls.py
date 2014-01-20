from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'llibreria.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'eines.views.home', name='home'),
    url(r'^llibres/', include('llibres.urls', namespace='llibres')),
    url(r'^prestecs/', include('prestecs.urls',namespace='prestecs')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^usuaris/', include('usuaris.urls', namespace='usuaris')),
    url('', include('social.apps.django_app.urls', namespace='social'))

)
