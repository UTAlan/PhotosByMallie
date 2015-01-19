from django.db import models
from django.forms import ModelForm

class ContactMessage(models.Model):
    name    = models.CharField(max_length=100)
    email   = models.EmailField()
    message = models.TextField()
    ip = models.CharField(max_length=15)
    date_sent = models.DateTimeField(auto_now_add=True)

class ContactMessageForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
