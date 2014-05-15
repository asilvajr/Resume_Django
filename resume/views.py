from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render
from resume.models import Technologies
# Create your views here.


def add_job(request):
    return None
def add_exp(request):    
    return None
def add_tech(request):
    if 'submit' in request.POST:
        submit_tech(request)
    techs = Technologies.objects.all()
    t = loader.get_template('tech_form.html')
    c = Context({'techs':techs})
    return render(request, 'tech_form.html',c)

def add_course(request):
    return None
    
def add_project(request):
    return None
    
def submit_job(request):
    vals = request.POST.dict()
    job = Jobs(Company=vals['company'],position=vals['position'],location=vals['location'],start_date=vals['start_date'],end_date=vals['end_date'])
    job.save()
    return render(request, 'job_form.html',vals)
    
def submit_exp(request):
    vals = request.POST.dict()
    exp = Experiences(event=vals['event'],decription=vals['exp_descript'],tech_exp=vals['technology'],job_exp=vals[''])
    exp.save()
    return render(request,'exp_form.html',vals)

def submit_tech(request):
    vals = request.POST.copy()
    if vals['tech_name']:
        exists=Technologies.objects.get(name=vals['tech_name'])
        if not exists:
            tech = Technologies(name=vals['tech_name'],tech_type=vals['tech_type'])
            tech.save()
        else:
            error=[]
            error.append(exists.name + " exists as a "+exists.tech_type)
            vals['error']=error
    else:
        error=[]
        error.append("Added Nothing, Text Feild was empty")
    return render(request, 'tech_form.html', vals)


def submit_course(request):
    vals = request.POST.dict()
    course = Courses(course_name=vals['name'],course_decription=vals['course_descript'])
    course.save()
    return render(request, 'course_form.html', vals)

def submit_project(request):
    vals = request.POST.dict()
    proj = Projects(tech_used=vals['tech_used'],proj_description=vals['proj_descript'],course_exp=vals['courses'])
    proj.save()
    return render(request, 'project_form.html',vals)

def add_update(request, option):
    t = loader.get_template('job_form.html')
    c = Context({})
    options={
        'job':add_job(request),
        'exp':add_exp(request),
        'tech':add_tech(request),
        'course':add_course(request),
        'project':add_project(request)
        }
    form_html = options[option]
    
    return form_html

