from dataclasses import field

from rest_framework.serializers import ModelSerializer
from habits.models import Habit
from habits.validators import (RewardValidator,
                               DurationValidator,
                               RelatedHabitValidator,
                               PleasantHabitValidator,
                               RegularityValidator,)

class HabitSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            RewardValidator(field_1="reward", field_2="related_habit"),
            DurationValidator(field="duration"),
            RelatedHabitValidator(field="related_habit"),
            PleasantHabitValidator(field="is_pleasant"),
            RegularityValidator(field_1="frequency_number", field_2="frequency_unit")
        ]