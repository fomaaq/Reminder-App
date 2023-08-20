'''
Module for launching the application in terms of sending reminders
'''
import schedule
import time
from remind_sender import do_remind

# Initiates the "check_remind" method every 1 minute
schedule.every(1).minutes.do(do_remind)

# Provides endless operation of the "schedule" library
while True:
    schedule.run_pending()
    time.sleep(1)
