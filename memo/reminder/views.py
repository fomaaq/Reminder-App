from django.shortcuts import redirect
from django.views.generic import ListView, FormView, UpdateView, DeleteView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import ReminderItem
from .forms import AddRemindForm, NewUserForm
from django.urls import reverse_lazy


class ReminderView(LoginRequiredMixin, ListView):
    '''
    Class for representing the main page of the application
    '''
    model = ReminderItem
    template_name = 'reminder.html'
    context_object_name = 'reminders'
    paginate_by = 3
    login_url = 'login/'

    def get_queryset(self):
        return ReminderItem.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Home page'
        return context


class AddRemindView(FormView):
    '''
    Class for creating a new reminder
    '''
    form_class = AddRemindForm
    template_name = 'add_remind.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        messages.success(self.request, "The remind was added successfully.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There are errors in the form.")
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Add new remind'
        return context


class EditRemindView(UpdateView):
    '''
    Class for editing an existing remind
    '''
    template_name = 'edit_remind.html'
    form_class = AddRemindForm
    model = ReminderItem

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        messages.success(self.request, "The remind was edited successfully.")
        return redirect('/')

    def form_invalid(self, form):
        messages.error(self.request, "There are errors in the form.")
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Edit remind'
        return context


class DeleteRemindView(DeleteView):
    '''
    Class for deleting remind
    '''
    model = ReminderItem
    template_name = 'delete_remind.html'
    success_url = '/'
    context_object_name = 'remind'
    extra_content = {'page_title': 'Delete remind'}

    def form_valid(self, form):
        messages.success(self.request, 'The remind was deleted successfully.')
        return super(DeleteRemindView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Delete remind'
        return context


class SignUpView(CreateView):
    '''
    Class for registering a new user
    '''
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    form_class = NewUserForm
    success_url = '/'
    extra_content = {'page_title': 'Sign Up'}

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        login(self.request, self.object)
        messages.success(self.request, 'You have successfully registered.')
        return form_valid

    def form_invalid(self, form):
        messages.error(self.request, "There are errors in the form.")
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Registration'
        return context


class LoginView(LoginView):
    '''
    Class for user authorization
    '''
    template_name = 'login.html'
    redirect_authenticated_user = True
    extra_content = {'page_title': 'Login'}

    def get_success_url(self):
        return reverse_lazy('memo')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Login'
        return context
