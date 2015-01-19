from django.contrib import admin
from django import forms
from about.models import About
from tinymce.widgets import TinyMCE

class AboutForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 150, 'rows': 30}))
    
    class Meta:
        model = About

class AboutAdmin(admin.ModelAdmin):
    form = AboutForm
    list_display = ('title',)

admin.site.register(About, AboutAdmin)
