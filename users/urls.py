from django.db import router
from django.urls import path
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import UserViewSet

app_name = "users"

router = SimpleRouter()
router.register("", UserViewSet, basename="users")

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(permission_classes=(AllowAny,)),name="login"),
    path("token/refresh/", TokenRefreshView.as_view(permission_classes=(AllowAny,)), name="token_refresh")
]
urlpatterns += router.urls