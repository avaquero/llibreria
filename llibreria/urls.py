from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'llibreria.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'eines.views.home', name='home'),
    url(r'^xat$', 'eines.views.xat', name='xat'),
    url(r'^recerca$', 'eines.views.recerca', name='recerca'),
    url(r'^llibres/', include('llibres.urls', namespace='llibres')),
    url(r'^prestecs/', include('prestecs.urls',namespace='prestecs')),
    url(r'^solicituds/', include('prestecs.urls',namespace='solicituds')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^usuaris/', include('usuaris.urls', namespace='usuaris')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
