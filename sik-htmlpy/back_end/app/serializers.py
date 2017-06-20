from rest_framework import serializers
from app.models import *


class QuestionSerializer(serializers.ModelSerializer):
    options = serializers.SlugRelatedField(many=True, 
                                           read_only=True,
                                           slug_field='detail')

    class Meta:
        model = Question
        fields = ('question_type', 'detail', 'options')


class TestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, 
                                   read_only=True)

    class Meta:
        model = Test
        fields = ('course', 'title', 'description', 'duration', 'instruction' ,'questions')


class CourseSerializer(serializers.ModelSerializer):
    tests = TestSerializer(many=True, 
                           read_only=True)

    class Meta:
        model = Course
        fields = ('name', 'code', 'tests')