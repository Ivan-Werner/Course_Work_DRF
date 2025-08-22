from django.db import router
from django.urls import path
from rest_framework.routers import SimpleRouter

from users.views import UserViewSet

app_name = "users"

router = SimpleRouter()
router.register("", UserViewSet, basename="users")

urlpatterns = [

]
urlpatterns += router.urls