# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from ..models import Student, Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from datetime import datetime

# Views for Students
def students_list(request):
    students = Student.objects.all()

    #try to order students_list
    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name', 'first_name', 'ticket','id'):
        students = students.order_by(order_by)
        if request.GET.get('reverse','') == '1':
            students = students.reverse()

    #paginate students
    paginator = Paginator(students, 3)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # If page not an integer, deliver first page
        students = paginator.page(1)
    except EmptyPage:
        # If page is not of range(e.g. 999), deliver last page of results
        students = paginator.page(paginator.num_pages)

    return render(request, 'students/students_list.html',
                  {'students': students})

# Views for Student Add Form
def students_add(request):
    # Was form posted?
    if request.method == "POST":
        # Was add button clicked?:
        if request.POST.get('add_button') is not None:
            #validate input user
            errors = {}

            data = {'middle_name': request.POST.get('middle_name'),
                    'notes': request.POST.get('notes')}

            #check user first name
            first_name = request.POST.get('first_name','').strip()
            if not first_name:
                errors['first_name'] = u"Імя є обов'язковим"
            else:
                data['first_name'] = first_name

            #check user last name
            last_name = request.POST.get('last_name','').strip()
            if not last_name:
                errors['last_name'] = u"Прізвище є обов'язковим"
            else:
                data['last_name'] = last_name

            #check birthday
            birthday = request.POST.get('birthday','').strip()
            if not birthday:
                errors['birthday'] = u"Дата народження є обов'язковою"
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors['birthday'] = \
                          u"Введіть коректний формат дати (напр. 1984-12-30)"
                else:
                    data['birthday'] = birthday

            #check ticket
            ticket = request.POST.get('ticket','').strip()
            if not ticket:
                errors['ticket'] = u"Білет є обов'язковим"
            else:
                data['ticket'] = ticket

            #check groups
            student_group = request.POST.get('student_group','').strip()
            if not student_group:
                errors['student_group'] = u"Група є обов'язковою"
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    errors['student_group'] = u"Оберіть коректну групу"
                else:
                    data['student_group'] = groups[0]

            #check photo
            photo = request.FILES.get('photo')
            if photo:
                data['photo'] = photo

            if not errors:
                # create Student object
                student = Student(**data)
                # save to db
                student.save()
                # redirect user to students list
                return HttpResponseRedirect(reverse('home'))
            else:
                #render form with errors and previous user input
                return render(request, 'students/students_add.html',
                              {'groups': Group.objects.all().order_by('title'),
                               'errors': errors})
        # Was cancel_button clicked?
        elif request.POST.get('cancel_button') is not None:
            # redirect to home page on cancel button
            return HttpResponseRedirect(reverse("home"))
    else:
        # initial form render
        return render(request, 'students/students_add.html',
                      {'groups': Group.objects.all().order_by('title')})
def students_edit(request, sid):
    return HttpResponse('<h1> Edit Student %s </h1>' % sid)
def students_delete(request, sid):
    return HttpResponse('<h1> Delete Student %s </h1>' % sid)
