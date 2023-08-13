# Custom module that contains methods for sending notifications at a set time

# importing django settings for the custom module to work
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'memo.settings')
django.setup()


# use a third-party library "schedule"
import schedule
import datetime
import time
from reminder.models import ReminderItem
from django.core.mail import send_mail
# import from the private settings file the email address from which notifications will be sent
from memo.security_settings import MY_EMAIL_HOST_USER
from django.contrib.auth.models import User


# method for sending notifications
def send_remind(remind):
    remind_item = ReminderItem.objects.get(id=remind.id)
    # django's built-in "send email" method is used
    send_mail(subject='Remind from Memo App',
              message=(f'Remind: {remind_item.title}\n'
                       f'At: {remind_item.remind_date.strftime("%d/%m/%Y")},\
                        {remind_item.remind_time.strftime("%H:%M")}\n'
                       f'{remind_item.content}'),
              recipient_list=[User.objects.get(pk=remind.user.id).email],
              from_email=MY_EMAIL_HOST_USER,
              )


# method for checking which notifications should be sent and sending them
def check_remind():
    reminders_list = ReminderItem.objects.filter(reminder_on=True, remind_date=datetime.date.today())
    current_time = datetime.datetime.now()
    for remind in reminders_list:
        remind_time = remind.remind_time
        if remind_time.hour == current_time.hour and remind_time.minute == current_time.minute:
            send_remind(remind)
            print('remind_send')


# initiates the "check_remind" method every 1 minute
schedule.every(1).seconds.do(check_remind)

# provides endless operation of the "schedule" library
while True:
    schedule.run_pending()
    time.sleep(1)
