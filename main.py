#I am going to create a desktop notification app to get a reminder to rest after every hour. 
# Your message and alert can be absolutely anything you want. 
# You can have a list of things you need to do in the day, week or month, 
# and the reminder app will constantly remind you of the same.

#For this task you need to install a Python library known as Plyer,
# which is used to access the hardware components of your system.
# This library can be easily installed by using the pip command; pip install pyler.

import time

from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "ALERT!!!",
            message = "Take a break Haet! It has been an hour!",
            timeout = 10
        )
        time.sleep(3600)


#After running the code, you will continuously receive notifications every hour or
# until the time you set due to the while loop defined in the code.


