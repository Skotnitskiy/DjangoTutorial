from django.db import models


class Group(models.Model):
    group_name = models.CharField(max_length=100, verbose_name='Group name')

    def __str__(self):
        return '%s' % self.group_name


class Student(models.Model):
    name = models.CharField(max_length=50, verbose_name='Full name')
    date_of_birth = models.DateField(verbose_name='Date of birth')
    group = models.ForeignKey(Group, verbose_name='Group', on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.name
