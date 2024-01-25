from .views import SubscriptionViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()

router.register(r'subscription', SubscriptionViewSet)

urlpatterns = [
    path('', include(router.urls))
]