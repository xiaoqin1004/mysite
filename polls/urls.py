from django.urls import path
from django.urls.converters import SlugConverter
from django.urls import register_converter
from django.conf.urls import url
from .import views
# register_converter(SlugConverter, 'question_id')

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

