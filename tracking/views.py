from django.contrib.auth.models import User, Group
from rest_framework import viewsets, authentication
from rest_framework import permissions

from tracking.serializers import GPSPointSerializer, DeviceSerializer, \
    TrackedUserSerializer, UserSerializer

from tracking.models import GPSPoint, Device, TrackedUser


class GPSPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = GPSPoint.objects.all()
    serializer_class = GPSPointSerializer
    permission_classes = [permissions.IsAuthenticated]


class DeviceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]


class TrackedUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = TrackedUser.objects.all()
    serializer_class = TrackedUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    ]


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
