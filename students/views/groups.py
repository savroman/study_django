# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from ..models import Group


# Views for Groups
def groups_list(request):
    groups = Group.objects.all()

    return render(request, 'students/groups_list.html', {'groups': groups})
def groups_add(request):
    return  HttpResponse('<h1> Groups add Form </h1>')
def groups_edit(request, gid):
    return  HttpResponse('<h1> Edit Group %s </h1>' % gid)
def groups_delete(request, gid):
    return  HttpResponse('<h1> Group Delete %s </h1>' % gid)
