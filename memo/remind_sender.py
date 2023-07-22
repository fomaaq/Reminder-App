import django
# import sys
import os
# sys.path.append('C:/projects/django_project_0/reminder_app/memo')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'memo.settings')
django.setup()

import schedule
import datetime
import time
from reminder.models import ReminderItem
from django.core.mail import send_mail
from django.contrib.auth.models import User


def send_remind(remind):
    remind_item = ReminderItem.objects.get(id=remind.id)
    send_mail(subject='Remind from Memo App',
              message=(f'Remind: {remind_item.title}\n'
                       f'At: {remind_item.remind_date.strftime("%d/%m/%Y")},\
                        {remind_item.remind_time.strftime("%H:%M")}\n'
                       f'{remind_item.content}'),
              recipient_list=[User.objects.get(pk=remind.user.id).email],
              from_email='veek47@gmail.com',
              )


def check_remind():
    reminders_list = ReminderItem.objects.filter(reminder_on=True, remind_date=datetime.date.today())
    current_time = datetime.datetime.now()
    for remind in reminders_list:
        remind_time = remind.remind_time
        if remind_time.hour == current_time.hour and remind_time.minute == current_time.minute:
            send_remind(remind)
            # print('email send')


schedule.every(5).seconds.do(check_remind)

while True:
    schedule.run_pending()
    time.sleep(1)
