from django.db import models

class Habit(models.Model):
    habit = models.CharField(max_length=150, verbose_name="Привычка")
    place_of_habit = models.CharField(max_length=150, verbose_name="Место где нужно выполнять привычку", blank=True, null=True)
    time_of_habit = models.TimeField(verbose_name="Время, когда выполняется привычка", blank=True, null=True)

