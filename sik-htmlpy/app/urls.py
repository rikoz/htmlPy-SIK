from django.conf.urls import url, include
from app.views import TestViewSet, StudentViewSet, AnswerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tests', TestViewSet)
router.register(r'students', StudentViewSet)
router.register(r'answers', AnswerViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]