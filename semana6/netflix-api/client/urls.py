from .views import ClientViewSet, ProfileViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()

router.register(r'client', ClientViewSet)
router.register(r'profile', ProfileViewSet)

urlpatterns = [
    path('', include(router.urls))
]
