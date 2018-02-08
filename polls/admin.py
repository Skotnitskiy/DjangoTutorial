from django.contrib import admin

from polls.models import Student
from polls.models import Group

admin.site.register(Student)
admin.site.register(Group)
