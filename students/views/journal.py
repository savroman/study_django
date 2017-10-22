# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views for Groups
def journal(request):
    students = Journal.objects.all()

    return render(request, 'students/journal.html', {'students': students})
