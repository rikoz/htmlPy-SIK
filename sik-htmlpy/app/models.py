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
        return self.code


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


class Application(models.Model):
    command = models.CharField(max_length=200)
    extension = models.CharField(max_length=7)
    icon = models.ImageField(upload_to='icons/%Y/%m/%d', blank=True, null=True)
    
    def admin_icon(self):
		return '<img src="{0}" width="80px">'.format(self.icon.url)

    def __str__(self):
        return self.command


class Question(models.Model):
    test = models.ForeignKey(Test, related_name='questions')
    number = models.PositiveIntegerField()
    question_type = models.CharField(help_text="shows the type of question",
                                     max_length=200,
                                     choices=CHOICES)
    detail = models.CharField(max_length=200, help_text="Question detail")

    def __str__(self):
        return self.detail


class QuestionFile(models.Model):
    question = models.ForeignKey(Question, related_name='files')
    name = models.CharField(max_length=200)
    app = models.ForeignKey(Application)
    location = models.FileField(upload_to='files/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return self.name


class QuestionImage(models.Model):
    question = models.ForeignKey(Question, related_name='images')
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='questionimages/%Y/%m/%d')


class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options')
    detail = models.CharField(max_length=200, help_text='detail of the option')

    def __str__(self):
        return self.detail


class Student(models.Model):
    course = models.ForeignKey(Course, related_name='students', null=True, blank=True)
    mat_number = models.CharField(max_length=10, unique=True)
    full_name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', null=True, blank=True)

    #def admin_photo(self):
	#	return '<img src="{0}" width="100px">'.format(self.photo.url)

    def __str__(self):
        return self.mat_number