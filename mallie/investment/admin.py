from django.contrib import admin
from django import forms
from investment.models import Investment
from tinymce.widgets import TinyMCE

class InvestmentForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 100, 'rows': 30}))
    
    class Meta:
        model = Investment

class InvestmentAdmin(admin.ModelAdmin):
    form = InvestmentForm
    list_display = ('title',)

admin.site.register(Investment, InvestmentAdmin)
