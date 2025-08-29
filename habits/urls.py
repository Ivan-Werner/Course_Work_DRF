from django.urls import path
from rest_framework.routers import SimpleRouter

from habits.views import HabitViewSet, PublicHabitListAPIView

app_name = "habits"

router = SimpleRouter()
router.register("", HabitViewSet, basename="habits")

urlpatterns = [
    path("public/", PublicHabitListAPIView.as_view(), name="public"),
] + router.urls
