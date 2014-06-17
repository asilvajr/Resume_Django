from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView, RedirectView
from mysite.views import front, current_datetime, hours_ahead,about_me, brz_miles
from resume.views import exp_form, tech_form, job_form, course_form, project_form, resume_view,test_div


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
    url(r'^resume',resume_view),
    url(r'^hours_ahead/plus/(\d{1,2})$',hours_ahead),
    url(r'^exp_form/$',exp_form),
    url(r'^tech_form/$',tech_form),
    url(r'^job_form/$',job_form),
    url(r'^course_form/$',course_form),
    url(r'^project_form/$',project_form),
    #url(r'^exp_form/(\d+)/$',exp_form),
    #url(r'^project_form/(\d+)/$',project_form),
    #url(r'^remove_exp/$',remove_exp),  
    #url(r'^remove_tech/$',remove_tech),
    #url(r'^remove_job/$',remove_job),
    #url(r'^modify_job',modify_job), 
    #url(r'^add_(\w+)/$',add_entry),
    #url(r'^remove_(\w+)/$',remove_entry),
    url(r'^test_div/$',test_div),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
