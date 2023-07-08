import schedule
from .models import ReminderItem
from django.core.mail import send_mail


def checkRemind():
    


def sendRemindView(rem_item):
    remind_item = ReminderItem.objects.get(id=rem_item)
    send_mail(subject='Remind from Memo App',
              message=remind_item.content,
              # TODO нужно придумать как устанавливать email пользователя
              recipient_list=['veek47@ya.ru', ]
              )
