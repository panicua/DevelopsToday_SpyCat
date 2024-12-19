from rest_framework import viewsets, permissions

from SpyCat.models import SpyCat
from SpyCat.serializers import SpyCatSerializer


class SpyCatViewSet(viewsets.ModelViewSet):
    queryset = SpyCat.objects.all()
    serializer_class = SpyCatSerializer
    permission_classes = [permissions.AllowAny]
