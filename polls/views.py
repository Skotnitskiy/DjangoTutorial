from django.shortcuts import render

from polls.models import Student


def students(request, group_name):
    students = Student.objects.filter(group__group_name=group_name)
    context = {'students': students}
    return render(request, 'polls/students.html', context)


def student_detail(request, student_id):
    student = Student.objects.filter(id=student_id).first()
    context = {'student': student}
    return render(request, 'polls/student_detail.html', context)
