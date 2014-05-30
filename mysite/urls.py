from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView, RedirectView
from mysite.views import front, current_datetime, hours_ahead,about_me, brz_miles
from resume.views import add_entry, remove_entry, modify_job, add_exp, add_tech, add_job, remove_exp, remove_tech, remove_job


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
    # url(r'^/static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
    url(r'^$', about_me, name='home'),
    url(r'^time/$',current_datetime),
    url(r'^brz_miles/',brz_miles),
    url(r'^hours_ahead/plus/(\d{1,2})$',hours_ahead),
    url(r'^exp_form/$',exp_form),
    url(r'^tech_from/$',tech_from),
    url(r'^job_form/$',job_from),
    #url(r'^remove_exp/$',remove_exp),  
    #url(r'^remove_tech/$',remove_tech),
    #url(r'^remove_job/$',remove_job),
    #url(r'^modify_job',modify_job), 
    #url(r'^add_(\w+)/$',add_entry),
    #url(r'^remove_(\w+)/$',remove_entry),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
