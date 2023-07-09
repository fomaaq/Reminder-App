from django.shortcuts import redirect
from django.views.generic import ListView, FormView, UpdateView, DeleteView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib import messages
from .models import ReminderItem
from .forms import AddRemindForm, NewUserForm
from django.urls import reverse_lazy
# from django.http import HttpResponseRedirect
# from django.core.mail import send_mail


# def reminderView(request):
#     reminder_items = ReminderItem.objects.all()
#     return render(request, 'reminder.html', {'all_items': reminder_items})

class ReminderView(ListView):
    model = ReminderItem
    template_name = 'reminder.html'


class AddRemindView(FormView):
    form_class = AddRemindForm
    template_name = 'add_remind.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class EditRemindView(UpdateView):
    template_name = 'edit_remind.html'
    form_class = AddRemindForm
    model = ReminderItem

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return redirect('/')


class DeleteRemindView(DeleteView):
    model = ReminderItem
    template_name = 'delete_remind.html'
    success_url = '/'
    context_object_name = 'remind'

    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(DeleteRemindView, self).form_valid(form)


class SignUpView(CreateView):
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    form_class = NewUserForm
    success_url = '/'

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        login(self.request, self.object)
        return form_valid


class LoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('memo')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


# def addReminderView(request):
#     form = AddRemindForm()
#     if request.method == "POST":
#         form = AddRemindForm(request.POST)
#         if form.is_valid():
#             rem_item = form.save(commit=False)
#             rem_item.save()
#             return redirect('/reminder')
#     else:
#         form = AddRemindForm()
#     return render(request, 'add_remind.html', {'form': form})


# def editRemindView(request, rem_item):
#     selected_item = get_object_or_404(ReminderItem, id=rem_item)
#     form = EditRemindForm()
#     if request.method == "POST":
#         form = EditRemindForm(request.POST, instance=selected_item)
#         if form.is_valid():
#             rem_item = form.save(commit=False)
#             rem_item.save()
#             return redirect('/reminder')
#     else:
#         form = EditRemindForm()
#     return render(request, 'edit_remind.html', {'form': form})


# def addReminderView(request):
#     new_content = request.POST['content']
#     new_item = ReminderItem(content=new_content)
#     new_item.save()
#     return HttpResponseRedirect('/reminder/')


# def deleteReminderView(request, rem_item):
#     selected_item = ReminderItem.objects.get(id=rem_item)
#     selected_item.delete()
#     return HttpResponseRedirect('/reminder/')


# def enableRemindView(request, rem_item):
#     selected_item = ReminderItem.objects.get(id=rem_item)
#     selected_item.reminder_on = request.POST['reminder_on']
#     selected_item.save()
#     return HttpResponseRedirect('/reminder/')


# def setRemindView(request, rem_item):
#     selected_item = ReminderItem.objects.get(id=rem_item)
#     selected_item.remind_date = request.POST['remind_date']
#     selected_item.save()
#     return HttpResponseRedirect('/reminder/')


# тестовая функция для проверки отправки сообщения
# def sendRemindView(request, rem_item):
#     remind_item = ReminderItem.objects.get(id=rem_item)
#     send_mail(subject='Remind from Memo App',
#               message=remind_item.content,
#               # TODO нужно придумать как устанавливать email пользователя
#               recipient_list=['veek47@ya.ru', ]
#               )
#     return HttpResponseRedirect('/reminder/')
