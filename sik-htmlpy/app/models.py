from django.db import models
from datetime import timedelta

CHOICES = (
        ('o', 'Objective'),
        ('t', 'Theory')
    )

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=200, help_text="name of course")
    code = models.CharField(max_length=6, help_text="course code")

    def __str__(self):
        return self.name


class Test(models.Model):
    course = models.ForeignKey(Course, related_name='tests')
    title = models.CharField(help_text="title of test", max_length=20,
                             blank=True,
                             null=True)
    description = models.TextField(help_text="description of test")
    instruction = models.TextField(help_text="instruction of test")
    duration = models.DurationField(help_text="How long will the test last", default=timedelta(minutes=60), null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    test = models.ForeignKey(Test, related_name='questions')
    question_type = models.CharField(help_text="shows the type of question",
                                     max_length=200,
                                     choices=CHOICES,
)

    detail = models.CharField(max_length=200, help_text="Question detail")

    def __str__(self):
        return self.detail


class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options')
    detail = models.CharField(max_length=200, help_text='detail of the option')
    selected = models.BooleanField(help_text="if option has been selected")

    def __str__(self):
        return self.detail