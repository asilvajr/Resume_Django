from django.template import Context, loader
from django.http import HttpResponse
import datetime


def hello(request):
    return HttpResponse("Hello world")


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def update_form(request):
    t = loader.get_template('job_form.html')
    c = Context({})
    return HttpResponse(t.render(c))
    #return render(request, 'update_form.html')


