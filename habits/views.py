from rest_framework import viewsets, generics
from habits.models import Habit
from habits.serializers import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
