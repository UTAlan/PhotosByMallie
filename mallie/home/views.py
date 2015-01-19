from django.shortcuts import render_to_response
from django.template import RequestContext
from home.models import HomeImage

def index(request):
    info = {}
    
    info['homeImages'] = HomeImage.objects.all().order_by('title').order_by('order')

    return render_to_response('home/index.html', { 'info': info }, context_instance=RequestContext(request))

