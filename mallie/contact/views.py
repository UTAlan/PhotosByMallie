from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from contact.models import ContactMessage, ContactMessageForm
from recaptcha.client import captcha
from datetime import datetime

def index(request):
    info = {}
    
    info['msg'] = ''
    info['form'] = ''
    
    if request.method == 'POST': # If the form has been submitted...
        info['form'] = ContactMessageForm(request.POST) # A form bound to the POST data
        if info['form'].is_valid(): # All validation rules pass
#            r = captcha.submit(request.POST['recaptcha_challenge_field'], request.POST['recaptcha_response_field'], settings.RECAPTCHA_PRIVATE_KEY, request.META['REMOTE_ADDR'])
#            if not r.is_valid:
#                info['msg'] = '<p class="error">Invalid Captcha. Please try again.</p>'
#            else:
                # Process the data in form.cleaned_data
                name = info['form'].cleaned_data['name']
                email = info['form'].cleaned_data['email']
                message = info['form'].cleaned_data['message']
                recipients = ['alan@alanbeam.net']
		
                contactMessage = ContactMessage()
		contactMessage.name = name
		contactMessage.email = email
		contactMessage.message = message
		x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
		if x_forwarded_for:
                    contactMessage.ip = x_forwarded_for.split(',')[-1].strip()
                else:
                    contactMessage.ip = request.META.get('REMOTE_ADDR')
                
                contactMessage.date_sent = datetime.now()
                
                send_mail('Contact Message From ' + name + ' (' + email + ') - PhotosByMallie.com', message, email, recipients)
		contactMessage.save()
                
                info['msg'] = '<p class="success">Message successfully sent.</p>'
                info['form'] = ContactMessageForm()
    else:
        info['form'] = ContactMessageForm() # An unbound form
    
    return render_to_response('contact/index.html', { 'info': info }, context_instance=RequestContext(request))

