from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50, verbose_name='Full name')
    date_of_birth = models.DateField(verbose_name='Date of birth')
    def __str__(self):
        return '%s'%(self.name)


class Group(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=100, verbose_name='Group name')
    def __str__(self):
        return '%s'%(self.group_name)