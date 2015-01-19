from django.shortcuts import render_to_response
from django.template import RequestContext
from investment.models import Investment

def index(request):
    info = {}
    
    info['investment'] = Investment.objects.get(pk=1)
    
    return render_to_response('investment/index.html', { 'info': info }, context_instance=RequestContext(request))

