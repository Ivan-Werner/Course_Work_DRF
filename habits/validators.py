from datetime import timedelta

from rest_framework.serializers import ValidationError


class RewardValidator:
    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __call__(self, value):
        data = dict(value)
        field_1_value = data.get(self.field_1)
        field_2_value = data.get(self.field_2)
        if field_1_value and field_2_value:
            raise ValidationError("Вы не можете одновременно заполнить поля вознаграждения и связанной привычки")


class DurationValidator:
    def __init__(self, field, max_seconds=120):
        self.field = field
        self.max_seconds = max_seconds

    def __call__(self, value):
        field_value = value.get(self.field)

        if field_value and field_value > timedelta(seconds=self.max_seconds):
            raise ValidationError(f"Время выполнения должно быть не больше {self.max_seconds} секунд")


class RelatedHabitValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        field_value = value.get(self.field)
        if field_value is None:
            return

        if not hasattr(field_value, "is_pleasant"):
            raise ValidationError("Объект не имеет атрибута is_pleasant")

        if not field_value.is_pleasant:
            raise ValidationError("В связанные привычки могут попадать только привычки с признаком приятной привычки.")


class PleasantHabitValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        data = dict(value)
        is_pleasant = data.get(self.field)

        if is_pleasant:
            reward = data.get("reward")
            related_habit = data.get("related habit")

            if reward not in (None, "") or related_habit not in (None, ""):
                raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки")


class RegularityValidator:
    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __call__(self, value):
        data = dict(value)
        num = data.get(self.field_1)
        unit = data.get(self.field_2)

        if num is None or unit is None:
            return

        try:
            num = float(num)
            if num < 0:
                raise ValidationError("Количество не может быть отрицательным")

            if unit == "minutes":
                frequency_in_days = num / (60 * 24)
            elif unit == "hours":
                frequency_in_days = num / 24
            elif unit == "days":
                frequency_in_days = num

            if frequency_in_days > 7:
                raise ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней")
        except:
            raise ValidationError(f"Некорректное значение для поля {self.field1}")
