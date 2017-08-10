from django.conf.urls import url, include
from app.views import TestViewSet, StudentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tests', TestViewSet)
router.register(r'students', StudentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]