from rest_framework import serializers


class InventoryViewSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)