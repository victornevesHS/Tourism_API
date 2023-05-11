from rest_framework import viewsets
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer