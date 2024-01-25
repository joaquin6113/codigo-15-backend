from .views import ContentViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()

router.register(r'content', ContentViewSet)

urlpatterns = [
    path('', include(router.urls))
]