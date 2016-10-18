# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views for Students
def students_list(request):
    students = (
    {'id':1,
     'first_name': u'Андрієнков',
     'last_name': u'Андрій',
     'ticket': 101,
     'image': 'img/empty.png'},
    {'id':2,
     'first_name': u'Богданич',
     'last_name': u'Богдан',
     'ticket': 201,
     'image': 'img/empty.png'},
    {'id':3,
     'first_name': u'Васильчук',
     'last_name': u'Василь',
     'ticket': 202,
     'image': 'img/empty.png'}
    )
    return render(request, 'students/students_list.html', {'students': students})
def students_add(request):
    return HttpResponse('<h1> Student add Form </h1>')
def students_edit(request, sid):
    return HttpResponse('<h1> Edit Student %s </h1>' % sid)
def students_delete(request, sid):
    return HttpResponse('<h1> Delete Student %s </h1>' % sid)
