from django.core.cache import cache
from django.db import transaction
from rest_framework import status
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from stores.models import Store
from stores.resources.serializers import StoreSerializer
from users.models import User


class StoreCreateViewSet(CreateModelMixin, GenericViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def create(self, request, user_hmac_code):
        cached_user_data = cache.get(user_hmac_code)
        if cached_user_data is None:
            return Response(
                {"error": "Url bulunamadı veya süresi dolmuş olabilir."},
                status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        with transaction.atomic():
            user = User.objects.create(**cached_user_data)
            serializer.validated_data["user"] = user
            from pprint import pprint
            pprint(serializer.__dict__)
            self.perform_create(serializer)

        cache.delete(user_hmac_code)
        return Response({"message": "E-ticaret hesap bilgileri kaydedildi."},
                        status=status.HTTP_201_CREATED)


class StoreListViewSet(ListModelMixin, GenericViewSet):
    queryset = Store.objects.all().order_by("-id")
    serializer_class = StoreSerializer
