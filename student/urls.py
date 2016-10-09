from django.conf.urls import url
from . import views

urlpatterns = patterns
    url(r'^$', 'views.students_list', name='home'),
