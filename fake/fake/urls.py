from django.conf.urls import patterns, include, url
from experiments import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fake.views.home', name='home'),
    # url(r'^fake/', include('fake.foo.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^tests/', views.tests, name='tests'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
