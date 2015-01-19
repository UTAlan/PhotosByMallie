from django.contrib import admin
from home.models import HomeImage

class HomeImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    ordering = ('order','title')

admin.site.register(HomeImage, HomeImageAdmin)
