from rest_framework.serializers import ModelSerializer
# from user.serializers import UserSerializer
# from subscription.serializers import SubscriptionSerializer
from .models import Client, Profile


class ClientSerializer(ModelSerializer):
    # user = UserSerializer(read_only=True)
    # subscription = SubscriptionSerializer(read_only=True)
    class Meta:
        model = Client
        fields = '__all__'


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'