
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <https://unlicense.org>


# This is a sample Python script that shows Win10Toast working, a package that allows calling Windows 10 notifications, running every n seconds
# Import the packages

# for notifications
from win10toast import ToastNotifier

# to allow the sleep() command
import time

# to check if idle
import win32api


# https://stackoverflow.com/questions/911856/detecting-idle-time-using-python
def getIdleTime():
    return (win32api.GetTickCount() - win32api.GetLastInputInfo()) / 1000.0


def print_notif(notif_length, notification_title, notification_text):

    toast = ToastNotifier()

    toast.show_toast(
        notification_title,
        notification_text,
        duration=notif_length,
        icon_path="icon.ico",
        threaded=True,
    )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Running my python script")

    # number of times the notification should pop up before stopping (set to -1 for endless)
    num_rep = 2
    curr_rep = 0

    # in seconds
    length_before_notification = 15
    length_of_break = 1

    # how long we must be idle before we stop the timer
    idle_time_reset = 10

    notif_title = "Title"
    notif_text = "Text"

    # Read the data from a settings file (https://www.w3schools.com/python/python_file_open.asp)
    file = open("settings.txt", "r")

    if not file.closed:

        # List version
        file_content = file.readlines()

        # we must convert the string data to int for numbers (https://docs.python.org/3/library/functions.html#int)
        num_rep = int(file_content[2])

        length_before_notification = int(file_content[5])
        length_of_break = int(file_content[8])
        notif_title = file_content[11]
        notif_text = file_content[14]
        idle_time_reset = int(file_content[17])
        file.close()




    # an endless loop
    while curr_rep != num_rep:
        curr_rep += 1

        # call the notification here
        print_notif(length_of_break, notif_title, notif_text)
        print("Break Duration: " + str(length_of_break))
        time.sleep(length_of_break)
        print("Break end")

        # pause the program for n seconds
        curr_elapsed_time = 0
        while curr_elapsed_time < length_before_notification:

            time.sleep(1)
            curr_elapsed_time += 1

            while getIdleTime() > idle_time_reset:
                print("idle")
                if getIdleTime() < idle_time_reset:
                    # reset the timer once we exit the loop
                    curr_elapsed_time = 0

                    print("Stop idle")
                    # break out of the loop once the idle time is less
                    break
