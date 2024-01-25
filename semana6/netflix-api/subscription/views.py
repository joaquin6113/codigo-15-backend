from rest_framework.viewsets import ModelViewSet
from .models import Subscription
from .serializers import SubscriptionSerializer


class SubscriptionViewSet(ModelViewSet):
    # Select from subscription
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer