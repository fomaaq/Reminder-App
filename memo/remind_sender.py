'''
Custom module that contains methods for check and sending reminder at a set time
'''

# Importing django settings for the custom module to work
import django
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'memo.settings')
django.setup()


# Use a third-party library "schedule"
import datetime
from reminder.models import ReminderItem
from django.core.mail import send_mail
from memo.security_settings import MY_EMAIL_HOST_USER
from django.contrib.auth.models import User


def send_remind(remind):
    '''
    Method for sending reminders
    '''
    remind_item = ReminderItem.objects.get(id=remind.id)
    remind_date = remind_item.remind_date.strftime("%d/%m/%Y")
    remind_time = remind_item.remind_time.strftime("%H:%M")

    send_mail(subject='Remind from Memo App',
              message=(f'Remind: {remind_item.title}\n'
                       f'At: {remind_date}, {remind_time}\n'
                       f'{remind_item.content}'),
              recipient_list=[User.objects.get(pk=remind.user.id).email],
              from_email=MY_EMAIL_HOST_USER)


def get_reminds():
    '''
    Method for getting reminders to sent
    '''
    reminders_list = ReminderItem.objects.filter(reminder_on=True, remind_date=datetime.date.today())
    current_time = datetime.datetime.now()
    reminders_to_send = get_reminders_to_send(reminders=reminders_list, now=current_time)

    return reminders_to_send


def get_reminders_to_send(reminders, now):
    '''
    Method for checking which reminders should be sent
    '''
    if reminders is None or now is None:
        return []

    reminders_to_send = []

    for remind in reminders:
        remind_time = remind.remind_time
        is_remind_to_send = remind_time.hour == now.hour and remind_time.minute == now.minute

        if is_remind_to_send:
            reminders_to_send.append(remind)

    return reminders_to_send


def do_remind():
    '''
    Method for getting reminders with "get_reminds" method and sending them
    '''
    reminders_to_send = get_reminds()
    for remind in reminders_to_send:
        send_remind(remind)
