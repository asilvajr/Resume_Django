from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from django.db.models import Q
from resume.models import Technologies, Experiences, Jobs, Courses, Projects
import yaml

stream = open("resume/static/text.yml","r")
yaml_dict = yaml.load(stream)

# Create your views here.
def test_div(request):
    print "Test View"
    print yaml.dump(yaml_dict)
    return HttpResponse("<h2> Go Big or Got Home </h2>")

def resume_view(request):
    vals = dict()
    vals['jobs'] = Jobs.objects.all()
    tech_queryset = Technologies.objects.all()
    vals['langs'] = tech_queryset.filter(tech_type="Language")
    vals['databases'] = tech_queryset.filter(tech_type="Databases") #MySql, sqlite3, MS-SQL
    vals['frameworks'] = tech_queryset.filter(tech_type="Framework") #django, #rails, #mason
    vals['tools_kits'] = tech_queryset.filter(
        Q(tech_type="Tools") | Q(tech_type="Kits")#Tools=wireshark, VI, sublime2 and #kits=bootstrap
        )
    vals['exps'] = Experiences.objects.all()
    vals['courses'] = Courses.objects.all() 
    vals['projs'] = Projects.objects.all()
    return render_to_response('resume_view.html',Context(vals))

def remove_job(request):
    return None

def remove_exp(request,job_):
    for exp_id in request.POST.getlist('rm_exps[]'):
        exp = Experiences.objects.get(id=exp_id)
        print "Exp to delete"+exp_id
        exp.delete()
    techs = Technologies.objects.all()
    exps_list = Experiences.objects.filter(job=job_)
    return render(request,'exp_form.html',Context({'techs':techs,'exps':exps_list}))
    
def remove_tech(request):
    tech_list = []
    if 'remove' in request.POST:
        for tech in request.POST.getlist('rm_techs[]'):
            t = Technologies.objects.get(name=tech)
            t.delete()
            tech_list.append(tech)
    techs = Technologies.objects.all()
    return Context({'techs':techs,'list':tech_list})
    #return render(request,'tech_form.html',Context({'techs':techs,'list':tech_list}))
    
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
        job_ = Jobs.objects.get(id=jid)
        exps = Experiences.objects.filter(job=job_)
        techs = Technologies.objects.all()
        return render_to_response('job_exp_form.html',{'job':job_,'techs':techs,'exps':exps})
    else:
        jobs = Jobs.objects.all()     
        return render_to_response('job_form.html',{'jobs':jobs})    
    
    
def add_exp(request,job_):
    vals = request.POST.dict()
    exp = Experiences(event=vals['event'],description=vals['exp_descript'])
    exp.job = job_
    exp.save()
    #print exp.event + "Was saved with exp_id" + exp.id
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
    return Context({'techs':techs})
    #return render_to_response('tech_form.html', {'techs':techs})


def add_course(request):
    vals = request.POST.dict()
    course = Courses(course_name=vals['course_name'],course_description=vals['course_description'])
    course.save()
    #load the add_project page
    projs = Projects.objects.filter(id=course.id)
    techs = Technologies.objects.all()
    return render_to_response('course_project_form.html', {'course':course,'projs':projs,'techs':techs})

def add_project(request,course_):
    vals = request.POST.dict()
    proj = Projects(proj_description=vals['proj_descript'])
    proj.courses = course_
    proj.save()
    for tid in request.POST.getlist('tech_used[]'):
        tech = Technologies.objects.get(id=tid)
        print "Tie-ing Tech ID to project_id" + str(proj.id) + "add_tech" + tech.name
        proj.tech_used.add(tech)
    projs = Projects.objects.filter(courses=course_)
    techs= Technologies.objects.all()
    return render_to_response('course_project_form.html',{'projs':projs,'added_proj':proj,'techs':techs,'course':course_})

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
        return remove_exp(request,job_)
    techs = Technologies.objects.all() #To load a list for the form.
    return render_to_response('job_exp_form.html',{'techs':techs,'exps':exps,'job':job_})

def job_form(request):
    if 'add' in request.POST:
        return add_job(request)
    if 'modify' in request.POST:
        return modify_job(request)
    jobs = Jobs.objects.all()
    return render_to_response('job_form.html',{'jobs':jobs}) 

def tech_form(request):
    if 'add' in request.POST:
        return add_tech(request)
    if 'remove' in request.POST:
        return remove_tech(request)
    techs = Technologies.objects.all().order_by('tech_type')
    return render_to_response('tech_form.html',{'techs':techs})
     
def course_form(request):
    if 'add' in request.POST:
        return add_course(request)
    if 'modify' in request.POST:
        return modify_course(request)
    courses = Courses.objects.all()
    return render_to_response('course_form.html',{'courses':courses})

def project_form(request):
    if 'course_id' in request.POST:
        course_ = Courses.objects.get(id=int(request.POST['course_id']))
        projects = Projects.objects.filter(courses=course_)
    else:
        course_ = None
        projects = Projects.objects.filter(courses_id__isnull=True)
    if 'add' in request.POST:
        return add_project(request,course_)
    if 'remove' in request.POST:
        return remove_project(request,course_)
    techs = Technologies.objects.all()
    return render_to_response('course_project_form.html',{'project':projects,'techs':techs,'course':course_})


