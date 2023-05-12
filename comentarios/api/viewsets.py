from rest_framework import viewsets
from core.models import Comentario
from .serializers import ComentarioSerializer

class ComentarioViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer