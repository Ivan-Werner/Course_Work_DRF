from django.db import router
from django.urls import path
from rest_framework.routers import SimpleRouter

from habits.views import HabitViewSet

app_name = "habits"

router = SimpleRouter()
router.register("", HabitViewSet, basename="habits")

urlpatterns = [

]
urlpatterns += router.urls