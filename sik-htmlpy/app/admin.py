from django.contrib import admin
from .models import *


class QuestionFileInline(admin.StackedInline):
    model = QuestionFile


class QuestionImageInline(admin.StackedInline):
    model = QuestionImage


class StudentInline(admin.TabularInline):
    model = Student


class OptionInline(admin.TabularInline):
    model = Option


class StudentAdmin(admin.ModelAdmin):
    list_display = ('mat_number', 'full_name', 'admin_photo')
    list_filter = ('course',)
    search_fields = ('mat_number', 'full_name')
    

class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'lecturers')
    search_fields = ('lecturers', 'title')
    inlines = [
        StudentInline,
    ]


class TestAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'duration', 'venue', 'date')
    list_filter = ('venue', 'date')
    search_fields = ('course__title', 'course__code')


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('command', 'extension', 'admin_icon')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('test', 'question_type', 'detail')
    list_filter = ('question_type',)
    search_fields = ('detail',)
    inlines = [
        OptionInline,
        QuestionFileInline,
        QuestionImageInline
    ]


admin.site.register(Course, CourseAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Student, StudentAdmin)
