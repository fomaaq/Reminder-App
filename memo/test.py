'''
Tests for "remind_sender" module
'''
from remind_sender import get_reminders_to_send


class MockReminder():
    def __init__(self, hour, minute):
        self.remind_time = MockRemindTime(hour=hour, minute=minute)

    def __eq__(self, obj):
        return self.remind_time == obj.remind_time


class MockRemindTime():
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __eq__(self, obj):
        return self.hour == obj.hour and self.minute == obj.minute


class MockNow():
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute


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


def test_single__get_reminders_to_send():
    reminders = [
        MockReminder(hour=10, minute=20),
    ]

    now = MockNow(hour=10, minute=20)

    expected = [
        MockReminder(hour=10, minute=20)
    ]

    actual = get_reminders_to_send(reminders=reminders, now=now)

    assert expected == actual


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


def test_multiply__get_reminders_to_send():
    reminders = [
        MockReminder(hour=10, minute=20),
        MockReminder(hour=12, minute=35),
        MockReminder(hour=22, minute=11),
        MockReminder(hour=8, minute=2),
        MockReminder(hour=10, minute=20),
        MockReminder(hour=3, minute=3),
        MockReminder(hour=14, minute=46),
    ]

    now = MockNow(hour=10, minute=20)

    expected = [
        MockReminder(hour=10, minute=20),
        MockReminder(hour=10, minute=20),
    ]

    actual = get_reminders_to_send(reminders=reminders, now=now)

    assert expected == actual


def test_empty__get_reminders_to_send():
    reminders = []

    now = MockNow(hour=0, minute=0)

    expected = []

    actual = get_reminders_to_send(reminders=reminders, now=now)

    assert expected == actual


def test_none__get_reminders_to_send():
    reminders = None

    now = MockNow(hour=0, minute=0)

    expected = []

    actual = get_reminders_to_send(reminders=reminders, now=now)

    assert expected == actual


def test_now_none__get_reminders_to_send():
    reminders = [
        MockReminder(hour=10, minute=20),
        MockReminder(hour=12, minute=35),
        MockReminder(hour=22, minute=11),
        MockReminder(hour=8, minute=2),
        MockReminder(hour=3, minute=3),
        MockReminder(hour=14, minute=46),
    ]

    now = None

    expected = []

    actual = get_reminders_to_send(reminders=reminders, now=now)

    assert expected == actual


def test_all_none__get_reminders_to_send():
    reminders = None

    now = None

    expected = []

    actual = get_reminders_to_send(reminders=reminders, now=now)

    assert expected == actual


if __name__ == "__main__":
    test_default__get_reminders_to_send()
    test_single__get_reminders_to_send()
    test_not_now__get_reminders_to_send()
    test_multiply__get_reminders_to_send()
    test_empty__get_reminders_to_send()
    test_none__get_reminders_to_send()
    test_now_none__get_reminders_to_send()
    test_all_none__get_reminders_to_send()
