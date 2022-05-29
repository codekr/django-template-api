from rest_framework import viewsets
from rest_framework.response import Response


class ZipcodeViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """

    def list(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass
