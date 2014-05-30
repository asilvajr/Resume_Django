from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render
from resume.models import Technologies, Experiences, Jobs
# Create your views here.

def remove_job(request):
    return None

def remove_exp(request):
    exp_list = []
    if 'remove' in request.POST:
        for exp_id in request.POST.getlist('rm_exps[]'):
            exp = Experiences.objects.get(id=exp_id)
            print "Exp to delete"+exp_id
            exp.delete()
    techs = Technologies.objects.all()
    exps_list = Experiences.objects.all()
    return render(request,'exp_form.html',Context({'techs':techs,'exps':exps_list}))
    
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
    
def add_job(request):
    vals = request.POST.dict()
    job = Jobs(company=vals['company'],position=vals['position'],location=vals['location'],start_date=vals['start_date'],end_date=vals['end_date'])
    job.save()
    #load the add experience page.
    exps = Experiences.objects.filter(id=job.id)
    techs = Technologies.objects.all()
    return render_to_response('job_exp_form.html',{'job':job,'exps':exps,'techs':techs})
    
def modify_job(request):
    vals=request.POST.dict()
    jid = vals.get('mod_jobs',None)
    if jid:
        job = Jobs.objects.get(id=jid)
        #load all the experiences related to the job.
        #add more experiences
        #submit
    else:
        jobs = Jobs.objects.all()     
        return render(request,'job_form.html',{'jobs':jobs})    
    techs = Technologies.objects.all()
    exps = Experiences.objects.filter()
    return render(request,'job_exp_form.html',{'job':job,'techs':techs})
    
    
def add_exp(requestjob_):
    vals = request.POST.dict()
    exp = Experiences(event=vals['event'],description=vals['exp_descript'])
    exp.job = job_
    exp.save()
    for tid in request.POST.getlist('tech_exps[]'):
        tech = Technologies.objects.get(id=tid)
        print "Vals" + vals['event'] + "added tech:" + tech.name
        exp.tech_exp.add(tech)
    exp.save()
    exps = Experiences.objects.filter(job=job_)
    techs = Technologies.objects.all()
    return render_to_response('job_exp_form.html',{'techs':techs,'exps':exps,'job':job_})

def add_tech(request):
    vals = request.POST.dict()
    vals['errors']=[]
    if vals.get('tech_name',None):
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
    techs = Technologies.objects.all()
    return render_to_response('tech_form.html', {'techs':techs})


def add_course(request):
    vals = request.POST.dict()
    course = Courses(course_name=vals['name'],course_decription=vals['course_descript'])
    course.save()
    #load the add_project page
    exps = Experience.objects.filter(id=job.id)
    techs = Technologies.objects.all()
    return render_to_response('course_project_form.html', {'course':course,'exps':exps,'techs':techs})

def add_project(request,course_):
    vals = request.POST.dict()
    proj = Projects(tech_used=vals['tech_used'],proj_description=vals['proj_descript'],course_exp=vals['courses'])
    proj.course = course_
    proj.save()
    for tid in request.POST.getlist('tech_used[]'):
        tech = Technologies.objects.get(id=tid)
        print "Tie-ing Tech ID to project_id" + proj.id + "add_tech" + tech.name
        proj.tech_used.add(tech)
    projs = Projects.objects.filter(course_id=course_)
    techs= Technologies.objects.all()
    return render_to_response('course_project_form.html',{'projs':projs,'proj':proj,'techs':techs,'course':course_})

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

def goto_form(request, option):
    print "Print Option in Url is: "+ option
    options={
        'job':job_form(request),
        'exp':exp_form(request),
        'tech':tech_form(request),
        'course':course_form(request),
        'project':project_form(request)}
    if option in options.keys():
	response = HttpResponse("there wasa an error loading " + option + ".")
        return options.get(option, response)
    else:
	return HttpResponse("This is the response: "+ option + ".")

def exp_form(request):
    job_ = Jobs.objects.get(id=int(request.POST['job_id']))
    exps = Experiences.objects.filter(job=job_)
    if 'add' in request.POST:
        return add_exp(request,job_)
    if 'remove' in request.POST:
        return remove_exp(request)
    techs = Technologies.objects.all() #To load a list for the form.
    return render_to_response('exp_form.html',{'techs':techs,'exps':exps,'job':job_})

def job_form(request):
    if 'add' in request.POST:
        return add_job(request)
    if 'modify' in request.POST:
        return modify_job(request)
    jobs = Jobs.objects.all()
    return render_tor_response('job_exp_form.html',{'jobs':jobs}) 

def tech_from(request):
    if 'add' in request.POST:
        return add_tech(request)
    if 'remove' in request.POST:
        return remove_tech(request)
    techs = Technologies.objects.all()
    return render_to_respons('tech_from.html',{'techs':techs})
     
def course_form(request):
    if 'add' in request.POST:
        return add_course(request)
    if 'modify' in request.POST:
        return modify_course(request)
    coures = Courses.objects.all()
    return render_to_response('course_form.html',{'courses':courses})

def project_from(request):
    if 'course_id' in request.POST:
        course_ = Courses.objects.get(id=request.POST['course_id'])
        projects = Projects.objects.filter(couse_id=course_)
    else:
        course_ = None
        projects = Projects.objects.filter(courses_id__isnull=True)
    if 'add' in request.POST:
        return add_project(request,course_)
    if 'remove' in request.POST:
        return remove_project(request,course_)
    techs = Projects.objects.all()
    return render_to_response('project_form.html',{'project':projects,'techs':techs,'course':course_})


