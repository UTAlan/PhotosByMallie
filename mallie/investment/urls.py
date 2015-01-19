from django.conf.urls import patterns, url

from investment import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
