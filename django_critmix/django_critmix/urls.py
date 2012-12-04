from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_critmix.views.home', name='home'),
    # url(r'^django_critmix/', include('django_critmix.foo.urls')),

    url(r'^critmixes/$', 'critmixes.views.index'),
    url(r'^critmixes/(?P<critmix_id>\d+)/$', 'critmixes.views.detail'),
    url(r'^critmixes/(?P<critmix_id>\d+)/results/$', 'critmixes.views.results'),
    url(r'^critmixes/(?P<critmix_id>\d+)/vote/$', 'critmixes.views.vote'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^savecrits/$', 'critmixes.views.savecrits'),
)
