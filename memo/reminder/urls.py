from django.urls import path
from reminder.views import ReminderView, AddRemindView, EditRemindView, DeleteRemindView, SignUpView, LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', ReminderView.as_view(), name='memo'),
    path('add_remind/', AddRemindView.as_view(), name='add_remind'),
    path('edit_remind/<int:pk>/', EditRemindView.as_view(), name='edit_remind'),
    path('edit_remind/<int:pk>/delete/', DeleteRemindView.as_view(), name='delete_remind'),
    path('login/register/', SignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='memo'), name='logout'),
]
