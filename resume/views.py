from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render
from resume.models import Technologies, Experiences
# Create your views here.

def add_job(request):
    return None
    
def add_exp(request):    
    if 'submit' in request.POST:
        return submit_exp(request)
    techs = Technologies.objects.all() #To load a list for the form.
    exps = Experiences.objects.all()
    return render(request, 'exp_form.html',{'techs':techs,'exps':exps})

def add_tech(request):
    if 'submit' in request.POST:
        return submit_tech(request)
    techs = Technologies.objects.all()
    return render(request, 'tech_form.html',{'techs':techs})

def add_course(request):
    return None
    
def add_project(request):
    return None

def remove_job(request):
    return None

def remove_exp(request):
    exp_list = []
    if 'remove' in request.POST:
        for exp_id in request.POST.getlist('rm_exp[]'):
            exp = Experiences.objects.get(id=exp_id)
            print "Exp to delete"+exp
            exp.delete()
    techs = Technologies.objects.all()
    exp_list = Experiences.objects.all()
    return render(request,'exp_form.html',Context({'techs':techs,'list':exp_list}))
    
def remove_tech(request):
    tech_list = []
    if 'remove' in request.POST:
        for tech in request.POST.getlist('rm_techs[]'):
            t = Technologies.objects.get(name=tech)
            t.delete()
            tech_list.append(tech)
    techs = Technologies.objects.all()
    return render(request,'tech_form.html',Context({'techs':techs,'list':tech_list}))
    
def remove_course(request):
    return None
    
def remove_project(request):
    return None
    
def submit_job(request):
    vals = request.POST.dict()
    job = Jobs(Company=vals['company'],position=vals['position'],location=vals['location'],start_date=vals['start_date'],end_date=vals['end_date'])
    job.save()
    return render(request, 'job_form.html',vals)
    
def submit_exp(request):
    vals = request.POST.dict()
    exp = Experiences(event=vals['event'],description=vals['exp_descript'])
    for tid in request.POST.getlist('exp_techs[]'):
        tech = Technologies.objects.get(id=tid)
        exp.Technologies.add(tech)
    exp.save()
    exps = Experiences.objects.all()
    techs = Technologies.objects.all()
    return render(request,'exp_form.html',{'techs':techs,'exps':exps})

def submit_tech(request):
    vals = request.POST.dict()
    vals['errors']=[]
    if vals['tech_name']:
        try:
            exists=Technologies.objects.get(name=vals['tech_name'])
        except Technologies.DoesNotExist:
            exists=None
        if not exists:
            tech = Technologies(name=vals['tech_name'],tech_type=vals['tech_type'])
            tech.save()
        else:
            vals['errors'].append(exists.name + "already exists as a " + exists.tech_type)
    else:
        vals['errors'].append("Added Nothing, Text Feild was empty")
    vals['techs'] = Technologies.objects.all()
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

def remove_entry(request,option):
    options={
        'job':remove_job(request),
        'exp':remove_exp(request),
        'tech':remove_tech(request),
        'course':remove_course(request),
        'project':remove_project(request)
        }
    form_html = options[option]
    return form_html

def add_entry(request, option):
    print "Print Option in Url is:"+option
    options={
        'job':add_job(request),
        'exp':add_exp(request),
        'tech':add_tech(request),
        'course':add_course(request),
        'project':add_project(request)
        }
    form_html = options[option]    
    return form_html

