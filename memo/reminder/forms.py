from django import forms
from django.db import models
from .models import ReminderItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# class for getting a standard django widget for entering a date
class DateInput(forms.DateInput):
    input_type = 'date'


# class for getting a standard django widget for entering time
class TimeInput(forms.TimeInput):
    input_type = 'time'


# form for creating and editing reminders
class AddRemindForm(forms.ModelForm):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)

    class Meta:
        model = ReminderItem
        fields = ('title', 'content', 'reminder_on', 'remind_date', 'remind_time')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'reminder_on': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'chk'}),
            # adding the django date entry widget
            'remind_date': DateInput,
            # adding the django time entry widget
            'remind_time': TimeInput,
        }

    def clean(self):
        cleaned_data = super().clean()
        reminder_on = cleaned_data.get('reminder_on')
        remind_date = cleaned_data.get('remind_date')
        remind_time = cleaned_data.get('remind_time')

        if reminder_on and (not remind_date or not remind_time):
            raise forms.ValidationError({
                'remind_date': 'Remind date field must be filled in when the "Enable reminder" checkbox is selected',
                'remind_time': 'Remind time field must be filled in when the "Enable reminder" checkbox is selected',
            })
        return cleaned_data


# class for creating a new user
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
