from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'students.view.students_list', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
