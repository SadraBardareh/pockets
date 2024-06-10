from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from .models import LapizuaPocket
from .serializers import LapizuaPocketSerializer

class LapizuaPocketViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin,
                           DestroyModelMixin, GenericViewSet):
    queryset = LapizuaPocket.objects.all()
    serializer_class = LapizuaPocketSerializer