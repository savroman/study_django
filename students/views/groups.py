# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

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
