from django import forms
from django.db import models
from .models import ReminderItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class DateInput(forms.DateInput):
    '''
    Class for getting a standard django widget for entering a date in a froms
    '''
    input_type = 'date'


class TimeInput(forms.TimeInput):
    '''
    Class for getting a standard django widget for entering time in a froms
    '''
    input_type = 'time'


class AddRemindForm(forms.ModelForm):
    '''
    Form for creating and editing reminders
    '''
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)

    class Meta:
        model = ReminderItem
        fields = ('title', 'content', 'reminder_on', 'remind_date', 'remind_time')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'reminder_on': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'chk'}),
            'remind_date': DateInput,
            'remind_time': TimeInput,
        }

    def clean(self):
        cleaned_data = super().clean()
        reminder_on = cleaned_data.get('reminder_on')
        remind_date = cleaned_data.get('remind_date')
        remind_time = cleaned_data.get('remind_time')

        is_datetime_fields_empty = not remind_date or not remind_time
        is_validation_error = reminder_on and is_datetime_fields_empty

        if is_validation_error:
            raise forms.ValidationError({
                'remind_date': 'Remind date field must be filled in when the "Enable reminder" checkbox is selected',
                'remind_time': 'Remind time field must be filled in when the "Enable reminder" checkbox is selected',
            })

        return cleaned_data


class NewUserForm(UserCreationForm):
    '''
    Form for creating a new user
    '''
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
