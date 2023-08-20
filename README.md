# Memo App
Reminder application based on Python Django Framework and Schedule library


## Preview

![Main_page_multiply.png](https://github.com/fomaaq/reminder_app/blob/main/pics/Main_page_multiply.png?raw=true)



## Built with

- [Django](https://docs.djangoproject.com/en/4.2/) - framework for creating a web application
- [Schedule](https://schedule.readthedocs.io/en/stable/) - library for performing tasks at a set time


## App creation motivation

I created this application Memo App to:
- create my own web application
- use django framework to create an application
- use a third-party library "Schedule"
- learn how to configure the interface of a web application using bootstrap
- learn how to use js scripts on web application pages


## Features

The function of checking the list of reminders that will need to be sent is covered by multiply [tests](https://github.com/fomaaq/reminder_app/blob/main/memo/test.py) to verify the correctness of the selection of reminders to be sent in various situations:

Function covered by tests:

```python
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
```

Test classes to test the function:

1) Test class simulating the basic web application model "ReminderItem":

```python
        class MockReminder():
            def __init__(self, hour, minute):
                self.remind_time = MockRemindTime(hour=hour, minute=minute)

            def __eq__(self, obj):
                return self.remind_time == obj.remind_time
```

2) Test class simulating the time for the 1st test class:

```python
        class MockRemindTime():
            def __init__(self, hour, minute):
                self.hour = hour
                self.minute = minute

            def __eq__(self, obj):
                return self.hour == obj.hour and self.minute == obj.minute
```

3) Test class simulating the current time::

```python
        class MockNow():
            def __init__(self, hour, minute):
                self.hour = hour
                self.minute = minute
```

An example of one of the tests when one of the reminders should be sent (standart situation):

```python
    def test_default__get_reminders_to_send():
        reminders = [
            MockReminder(hour=10, minute=20),
            MockReminder(hour=12, minute=35),
            MockReminder(hour=22, minute=11),
            MockReminder(hour=8, minute=2),
            MockReminder(hour=3, minute=3),
            MockReminder(hour=14, minute=46),
        ]

        now = MockNow(hour=10, minute=20)

        expected = [
            MockReminder(hour=10, minute=20)
        ]

        actual = get_reminders_to_send(reminders=reminders, now=now)

        assert expected == actual
```

An example of one of the tests when it is impossible to get the current time:

```python
    def test_not_now__get_reminders_to_send():
        reminders = [
            MockReminder(hour=10, minute=20),
            MockReminder(hour=12, minute=35),
            MockReminder(hour=22, minute=11),
            MockReminder(hour=8, minute=2),
            MockReminder(hour=3, minute=3),
            MockReminder(hour=14, minute=46),
        ]

        now = MockNow(hour=0, minute=0)

        expected = []

        actual = get_reminders_to_send(reminders=reminders, now=now)

        assert expected == actual
```

## How to use

To use the app, you need to:
1) Go to the application page

![Login_page.png](https://github.com/fomaaq/reminder_app/blob/main/pics/Login_page.png?raw=true)

2) Register

![Register_page.png](https://github.com/fomaaq/reminder_app/blob/main/pics/Register_page.png?raw=true)

3) Click the "add a new reminder" button

![Main_view_empty.png](https://github.com/fomaaq/reminder_app/blob/main/pics/Main_view_empty.png?raw=true)

4) Create your own reminders and set the date and time of the reminder

![Create_reminder.png](https://github.com/fomaaq/reminder_app/blob/main/pics/Create_reminder.png?raw=true)
![Create_reminder_filled.png](https://github.com/fomaaq/reminder_app/blob/main/pics/Create_reminder_filled.png?raw=true)
![Main_page_single.png](https://github.com/fomaaq/reminder_app/blob/main/pics/Main_page_single.png?raw=true)

5) Get notifications to the email address specified during registration at the set time

![Example_reminder_1.png](https://github.com/fomaaq/reminder_app/blob/main/pics/Example_reminder_1.png?raw=true)

Also in the app you can: 
- edit existing reminders

![Edit_view.png](https://github.com/fomaaq/reminder_app/blob/main/pics/Edit_view.png?raw=true)

- delete unnecessary reminders

![Delete_view.png](https://github.com/fomaaq/reminder_app/blob/main/pics/Delete_view.png?raw=true)
![Succesfully_deleted.png](https://github.com/fomaaq/reminder_app/blob/main/pics/Succesfully_deleted.png?raw=true)

- create multiple users who will have their own reminders that are not available to other users

![Main_page_User_2.png](https://github.com/fomaaq/reminder_app/blob/main/pics/Main_page_User_2.png?raw=true)
![Main_page_User_2_single.png](https://github.com/fomaaq/reminder_app/blob/main/pics/Main_page_User_2_single.png?raw=true)


## How to run
Python version 3.11, Django version 4.2 and Schedule version 1.2 was used at launch

Detailed information about the requirements is provided in the [requirements.txt](https://github.com/fomaaq/reminder_app/blob/main/requirements.txt)
