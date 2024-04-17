from django.urls import include, path
from rest_framework.routers import DefaultRouter

from stores.resources.views import StoreCreateViewSet, StoreListViewSet
from users.resources.views import UserViewSet

router = DefaultRouter()
router.register("users", UserViewSet, "users")

urlpatterns = [
    path("", include(router.urls)),
    # stores
    path(
        "stores/",
        StoreListViewSet.as_view({'get': 'list'}),
        name="store-list"
    ),
    path(
        "stores/<str:user_hmac_code>/",
        StoreCreateViewSet.as_view({'post': 'create'}),
        name="store-create"
    ),
]
