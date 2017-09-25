from rest_framework import viewsets
from rest_framework import generics

from app.serializers import TestSerializer, AnswerSerializer, StudentSerializer
from app.models import Test, Student, Answer


class TestViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    This is the viewset for the Test model 
    '''
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    lookup_field = 'password'


class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    This is the viewset for the Test model 
    '''
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'mat_number'


class AnswerViewSet(viewsets.ModelViewSet):
    '''
    This is the viewset for the Answer model 
    '''
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    #http_method_names = ['post',]
