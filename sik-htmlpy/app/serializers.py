from rest_framework import serializers
from app.models import *


class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = ('id', 'command', 'extension', 'icon')


class QuestionFileSerializer(serializers.ModelSerializer):
    app = ApplicationSerializer()
    
    class Meta:
        model = QuestionFile
        fields = ('id', 'name', 'app', 'location')


class QuestionImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = QuestionImage
        fields = ('id', 'title', 'image')


class OptionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Option
        fields = ('id', 'detail')


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)
    images = QuestionImageSerializer(many=True, read_only=True)
    files = QuestionFileSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'number', 'question_type', 'detail', 'options',
            'images', 'files')


class TestSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.title')
    course_code = serializers.CharField(source='course.code')
    course_lecturers = serializers.CharField(source='course.lecturers')
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Test
        fields = ('id', 'course_title', 'course_code', 'course_lecturers', 'title', 
            'description', 'duration', 'instruction' ,'questions', 'venue', 'date')


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'