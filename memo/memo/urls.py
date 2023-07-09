"""
URL configuration for memo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from reminder.views import ReminderView, AddRemindView, EditRemindView, DeleteRemindView, SignUpView, LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ReminderView.as_view(), name='memo'),
    path('add_remind/', AddRemindView.as_view(), name='add_remind'),
    path('edit_remind/<int:pk>/', EditRemindView.as_view(), name='edit_remind'),
    path('edit_remind/<int:pk>/delete/', DeleteRemindView.as_view(), name='delete_remind'),
    path('login/register/', SignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='memo'), name='logout'),
    # # path('reminder/', reminderView),
    # path('reminder/add_remind/', addReminderView, name='add_remind'),
    # path('deleteReminderItem/<int:rem_item>/', deleteReminderView),
    # path('reminder/edit_remind/<int:rem_item>/', editReminderView, name='edit_remind'),
    # path('setRemindDate/<int:rem_item>/', setRemindView),
    # path('sendRemindEmail/<int:rem_item>/', sendRemindView),
    # path('enableRemind/<int:rem_item>/', enableRemindView),
]
