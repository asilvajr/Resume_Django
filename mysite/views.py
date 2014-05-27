from django.template import Context, Template, loader
from django.template.loader import get_template
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from datetime import *


def front(request):
    return render(request,"me.html",{})

def about_me(request):
    return render_to_response("about.html")

def brz_miles(request,plus=1):

    mpweek = lambda x : x * 288.461538
    mpday = lambda y : y * 41.2087912
    start = date(2013,11,22)
    end = datetime.now().date()
    delta = (end - start).days
    weeks = delta / 7
    days = delta % 7
    mileage_allowance = mpweek(weeks)  + mpday(days)
    mileage_plus = mpweek(weeks+plus)
    template = get_template('brz_miles.html')
    html= template.render(Context({'mileage_allowance':mileage_allowance,'mileage_plus':mileage_plus,'weeks':weeks,'days':days})) 
    return HttpResponse(html)

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

