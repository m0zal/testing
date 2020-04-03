from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from api_testing.models import Pril
from api_testing.serializers import PrilSerializer


class TestViewSet(viewsets.ModelViewSet):
    queryset = Pril.objects.all()
    serializer_class = PrilSerializer

    @action(detail=False, methods=["get"], url_path=r"test/(?P<api_key>[^/.]+)")
    def test(self, request, api_key, pk=None):
        pril = get_object_or_404(Pril, api_key=api_key)
        s = PrilSerializer(instance=pril)
        return Response(s.data)
