from django.conf.urls import patterns, include, url
from mysite.views import hello, current_datetime, hours_ahead
from resume.views import add_entry, remove_entry

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.hello', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'mysite.views.hello', name='home'),
    url(r'^time/$',current_datetime),
    url(r'^hours_ahead/plus/(\d{1,2})$',hours_ahead),
    url(r'^add_(\w+)/$',add_entry),
    url(r'^remove_(\w+)/$',remove_entry),
)
