from rest_framework import serializers

from stores.models import Store


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'store_url', 'platform', 'user']
        read_only_fields = ['user']
