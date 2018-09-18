from django.urls import path
from django.urls.converters import SlugConverter
from django.urls import register_converter

from .import views
# register_converter(SlugConverter, 'question_id')

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

