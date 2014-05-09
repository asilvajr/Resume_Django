from django.conf.urls import patterns, include, url
from mysite.views import hello, current_datetime, hours_ahead,job_update, tech_update,course_update,exp_update 


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
    url(r'^job_update/',job_update),
    url(r'^tech_update/',tech_update),
    url(r'^course_update/',course_update),
    url(r'^experience_update/',exp_update),
    url(r'^add_',add_update),
    
)
