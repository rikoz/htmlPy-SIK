from django.db import models
from datetime import timedelta


CHOICES = (
        ('o', 'Objective'),
        ('t', 'Theory')
    )


class Course(models.Model):
    title = models.CharField(max_length=200, help_text="title of course")
    code = models.CharField(max_length=6, help_text="course code")
    lecturers = models.TextField()

    def __str__(self):
        return self.title


class Test(models.Model):
    password = models.CharField(max_length=20, unique=True)
    course = models.ForeignKey(Course, related_name='tests')
    title = models.CharField(help_text="title of test", max_length=20,
                             blank=True,
                             null=True)
    description = models.TextField(help_text="description of test")
    instruction = models.TextField(help_text="instruction of test")
    duration = models.PositiveIntegerField()
    venue = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __str__(self):
        return self.title


class Question(models.Model):
    test = models.ForeignKey(Test, related_name='questions')
    question_type = models.CharField(help_text="shows the type of question",
                                     max_length=200,
                                     choices=CHOICES)

    detail = models.CharField(max_length=200, help_text="Question detail")

    def __str__(self):
        return self.detail


class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options')
    detail = models.CharField(max_length=200, help_text='detail of the option')
    selected = models.BooleanField(help_text="if option has been selected")

    def __str__(self):
        return self.detail


class Student(models.Model):
    mat_number = models.CharField(max_length=10, unique=True)
    full_name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.mat_number