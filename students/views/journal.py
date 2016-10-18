# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views for Groups
def journal(request):
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
    return render(request, 'students/journal.html', {'students': students})
