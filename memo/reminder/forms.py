from django import forms
from django.db import models
from .models import ReminderItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AddRemindForm(forms.ModelForm):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)

    class Meta:
        model = ReminderItem
        fields = ('title', 'content', 'reminder_on', 'remind_date', 'remind_time')
        widgets = {
            'remind_date': forms.DateInput(attrs={'class': 'form-control'}),
            'remind_time': forms.TimeInput(attrs={'class': 'form-control'}, format='%H:%M'),
        }
        help_texts = {
            'remind_date': 'Format should be "YYYY-MM-DD"',
            'remind_time': 'Format should be "HH:MM"',
        }


class NewUserForm(UserCreationForm):
    username = forms.CharField(label='User name',
                               max_length=150,
                               help_text='User name must consist of a maximum of 150 characters'
                               )
    email = forms.EmailField(label='e-mail', required=True)
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

# TODO созадть форму для редактирования пользователя
# class UpdateUserForm(forms.ModelForm):
#     username = forms.CharField(max_length=100,
#                                required=True,
#                                widget=forms.TextInput(attrs={'class': 'form-control'}))
#     email = forms.EmailField(required=True,
#                              widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password = forms.PasswordInput(re
#                                    widget=forms.PasswordInput(attrs={'class': 'form-control'}))

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
