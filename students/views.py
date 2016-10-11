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

# Views for Groups
def groups_list(request):
    groups = (
    {'id':1,
     'name': u'МтМ-21',
     'group_lider': u'Андрієнко Андрій'},
    {'id':2,
     'name': u'МтМ-22',
     'group_lider': u'Романович Роман'},
    {'id':3,
     'name': u'МтМ-23',
     'group_lider': u'Яремчук Ярема'},
    )
    return render(request, 'students/groups_list.html', {'groups': groups})
def groups_add(request):
    return  HttpResponse('<h1> Groups add Form </h1>')
def groups_edit(request, gid):
    return  HttpResponse('<h1> Edit Group %s </h1>' % gid)
def groups_delete(request, gid):
    return  HttpResponse('<h1> Group Delete %s </h1>' % gid)
