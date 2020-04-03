from django.db import transaction
from rest_framework import serializers
from api_testing import models


class PrilSerializer(serializers.ModelSerializer):

    api_key = serializers.CharField(read_only=True, )

    class Meta:
        model = models.Pril
        fields = ("id", "name", "api_key")

    @transaction.atomic()
    def save(self, **kwargs):
        super().save(**kwargs)
        self.instance.set_api_key()
