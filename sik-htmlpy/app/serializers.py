from rest_framework import serializers
from app.models import *


class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = ('id', 'command', 'extension', 'icon')


class QuestionFileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = QuestionFile
        fields = ('name', 'app', 'location')


class QuestionImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = QuestionImage
        fields = ('title', 'image')


class QuestionSerializer(serializers.ModelSerializer):
    options = serializers.SlugRelatedField(many=True, 
                                           read_only=True,
                                           slug_field='detail')
    images = QuestionImageSerializer(many=True, read_only=True)
    files = QuestionFileSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('question_type', 'detail', 'options',
            'images', 'files')


class TestSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.title')
    course_code = serializers.CharField(source='course.code')
    course_lecturers = serializers.CharField(source='course.lecturers')
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Test
        fields = ('course_title', 'course_code', 'course_lecturers', 'title', 
            'description', 'duration', 'instruction' ,'questions', 'venue', 'date')


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'