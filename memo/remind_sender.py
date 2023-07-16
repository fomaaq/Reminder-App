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
# from django.core.mail import send_mail


def check_remind():
    reminders_list = ReminderItem.objects.filter(reminder_on=True, remind_date=datetime.date.today())
    current_time = datetime.datetime.now()
    print(current_time)
    for remind in reminders_list:
        remind_time = remind.remind_time
        print(remind_time)
        if remind_time.hour == current_time.hour and remind_time.minute == current_time.minute:
            print('Send remind')


schedule.every(1).seconds.do(check_remind)

while True:
    schedule.run_pending()
    time.sleep(1)


# def sendRemindView(rem_item):
#     remind_item = ReminderItem.objects.get(id=rem_item)
#     send_mail(subject='Remind from Memo App',
#               message=remind_item.content,
#               # TODO нужно придумать как устанавливать email пользователя
#               recipient_list=['veek47@ya.ru', ]
#               )
