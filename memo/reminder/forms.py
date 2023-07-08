from django import forms
from django.db import models
from .models import ReminderItem


# class AddRemindForm(forms.Form):
#     content = forms.CharField(max_length=200, widget=forms.TextInput)
#     reminder_on = forms.BooleanField(required=False, initial=True)
#     remind_date = forms.DateTimeField(required=False, widget=forms.DateTimeInput)


class AddRemindForm(forms.ModelForm):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)

    class Meta:
        model = ReminderItem
        fields = ('title', 'content', 'reminder_on', 'remind_date', 'remind_time')
        widgets = {
            'remind_date': forms.DateInput(),
            'remind_time': forms.TimeInput(),
        }
        help_texts = {
            'remind_date': 'Format should be "YYYY-MM-DD"',
            'remind_time': 'Format should be "HH:MM"',
        }
