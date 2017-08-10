from django.contrib import admin
from .models import Test, Course, Question, Option, Student
# Register your models here.

admin.site.register(Course)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Student)