from django.shortcuts import render_to_response
from django.template import RequestContext
from about.models import About

def index(request):
    info = {}
    
    info['about'] = About.objects.get(pk=1)
    
    return render_to_response('about/index.html', { 'info': info }, context_instance=RequestContext(request))

