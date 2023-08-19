from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class ReminderItem(models.Model):
    '''
    Main application model
    '''
    title = models.CharField(max_length=50, verbose_name='title')
    content = models.TextField(max_length=1000, verbose_name='Content', blank=True)
    reminder_on = models.BooleanField(verbose_name='Remind enable')
    remind_date = models.DateField(blank=True, null=True, verbose_name='Remind date')
    remind_time = models.TimeField(blank=True, null=True, verbose_name='Remind time')
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("delete_remind", kwargs={"pk": self.pk})
