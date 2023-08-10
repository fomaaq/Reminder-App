from django import forms
from django.db import models
from .models import ReminderItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


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
            'remind_date': DateInput,
            'remind_time': TimeInput,
        }

    def clean(self):
        error_message = 'Remind date and time fields must be filled in when the "Enable reminder" checkbox is selected'
        cleaned_data = super().clean()
        reminder_on = cleaned_data.get('reminder_on')
        remind_date = cleaned_data.get('remind_date')
        remind_time = cleaned_data.get('remind_time')

        if reminder_on and (not remind_date or not remind_time):
            raise forms.ValidationError(error_message)
        return cleaned_data


class NewUserForm(UserCreationForm):
    username = forms.CharField(label='User name',
                               max_length=150,
                               help_text='User name must consist of a maximum of 150 characters'
                               )
    email = forms.EmailField(label='e-mail', required=True)
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm password',
                                widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
