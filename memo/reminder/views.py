from django.shortcuts import render
from .models import ReminderItem
from django.http import HttpResponseRedirect
from django.core.mail import send_mail


def reminderView(request):
    reminder_items = ReminderItem.objects.all()
    return render(request, 'reminder.html', {'all_items': reminder_items})


def addReminderView(request):
    new_content = request.POST['content']
    new_item = ReminderItem(content=new_content)
    new_item.save()
    return HttpResponseRedirect('/reminder/')


def deleteReminderView(request, rem_item):
    selected_item = ReminderItem.objects.get(id=rem_item)
    selected_item.delete()
    return HttpResponseRedirect('/reminder/')


def setRemindView(request, rem_item):
    selected_item = ReminderItem.objects.get(id=rem_item)
    selected_item.remind_date = request.POST['remind_date']
    selected_item.save()
    return HttpResponseRedirect('/reminder/')


def sendRemindView(request, rem_item):
    remind_item = ReminderItem.objects.get(id=rem_item)
    send_mail(subject='Remind from Memo App',
              message=remind_item.content,
              # TODO нужно придумать как устанавливать email пользователя
              recipient_list=['veek47@ya.ru', ]
              )
    return HttpResponseRedirect('/reminder/')
