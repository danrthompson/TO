from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TO.views.home', name='home'),
    # url(r'^TO/', include('TO.foo.urls')),

(r'^home/$', 'views.home'),
(r'^new_profile/$', 'profiles.views.new_profile'),
(r'^create_profile/$', 'profiles.views.create_profile'),
(r'^login/$', 'views.login'),
(r'^check_auth/$', 'views.check_auth'),
(r'^private_page/$', 'views.private_page'),

    # Uncomment the admin/doc line below to enable admin documentation:
(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
 url(r'^admin/', include(admin.site.urls)),
)
