from django.db import models
from django.core.validators import MinValueValidator


class ReminderItem(models.Model):
    content = models.TextField(verbose_name='Content')
    remind_date = models.IntegerField(blank=True, validators=[MinValueValidator(0)], verbose_name='Remind date')

    """
    + напоминать/не напоминать
    + время + дата напоминания
    + повтор напоминания*
    """
