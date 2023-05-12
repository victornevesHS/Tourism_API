from rest_framework import viewsets
from core.models import Atracao
from .serializers import AtracaoSerializer

class AtracaoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer