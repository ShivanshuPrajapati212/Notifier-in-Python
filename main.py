from win10toast import ToastNotifier
import pandas as pd

def show_notification(title, message):
    toaster = ToastNotifier()
    toaster.show_toast(title, message, duration=2)


if __name__ == "__main__":
    task = input("Enter the Name of Task: ")
    desc = input("Give some Description about the task: ")
    time  = input("Enter the Time to Schedule (22:00): ")

    show_notification(task, desc)
