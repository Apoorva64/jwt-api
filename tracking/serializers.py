from django.contrib.auth.models import User
from rest_framework import serializers

from tracking.models import GPSPoint, Device, TrackedUser


class GPSPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPSPoint
        fields = ('lat', 'lon', 'timestamp')


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('name', 'gps')


class TrackedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackedUser
        fields = ('name', 'devices')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
