from rest_framework.decorators import api_view
from rest_framework import viewsets
from app.serializers import TestSerializer, CourseSerializer, QuestionSerializer
from app.models import Test, Course, Question
from rest_framework.response import Response

class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    This is the viewset for the Test model 
    '''
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def list(self, request):
        course_queryset = Course.objects.all()
        test_queryset = Test.objects.all()
        questions_queryset = Question.objects.all()

        course_serializer = CourseSerializer(course_queryset, many=True)
        test_serializer = TestSerializer(test_queryset, many=True)
        question_serializer = QuestionSerializer(questions_queryset, many=True)

        response = course_serializer.data + test_serializer.data + question_serializer.data

        return Response(response)