from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from datetime import datetime

from polls.models import Student, Group


def students(request, group_name):
    students = Student.objects.filter(group__group_name=group_name)
    groups = Group.objects.all()
    context = {'students': students,
               'groups': groups
               }
    return render(request, 'polls/students.html', context)


def student_detail(request, student_id):
    student = Student.objects.get(pk=student_id)
    context = {'student': student}
    return render(request, 'polls/student_detail.html', context)


def add_student(request):
    student_name = request.POST.get('name')
    group_id = request.POST.get('group')
    birthday = datetime.today()
    new_sudent = Student(name=student_name, date_of_birth=birthday, group_id=group_id)
    new_sudent.save()
    return redirect(request.META['HTTP_REFERER'])
