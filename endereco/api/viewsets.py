from rest_framework import viewsets
from endereco.models import Endereco
from .serializers import EnderecoSerializer


class EnderecoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer