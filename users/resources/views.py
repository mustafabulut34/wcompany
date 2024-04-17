from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from django.urls import reverse
from rest_framework.viewsets import GenericViewSet

from stores.generators import generate_user_hmac
from users.models import User
from users.resources.serializers import UserSerializer


class UserViewSet(ListModelMixin, CreateModelMixin, GenericViewSet):
    queryset = User.objects.all().order_by("-id")
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        phone_number = serializer.validated_data["phone_number"]

        user_hmac_code = generate_user_hmac(email, phone_number)
        cache.set(user_hmac_code, serializer.validated_data, timeout=300)

        next_url = reverse('store-create',
                           kwargs={'user_hmac_code': user_hmac_code})

        return Response(
            {
                "message": "next_url'i kullanarak işleminizi "
                           "tamamlayabilirsiniz. next_url 5 dakika içerisinde "
                           "kullanılmalıdır.",
                "next_url": next_url
            },
            status=status.HTTP_200_OK
        )
