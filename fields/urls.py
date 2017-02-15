from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.fields, name='fields'),
    url(r'^script$', views.script, name='script'),
    url(r'^output$', views.output, name='output'),
    url(r'^clearDB$', views.cleardb, name='clearDB'),
]