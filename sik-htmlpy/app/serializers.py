from rest_framework import serializers
from app.models import Test, Student, Question


class QuestionSerializer(serializers.ModelSerializer):
    options = serializers.SlugRelatedField(many=True, 
                                           read_only=True,
                                           slug_field='detail')

    class Meta:
        model = Question
        fields = ('question_type', 'detail', 'options')


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