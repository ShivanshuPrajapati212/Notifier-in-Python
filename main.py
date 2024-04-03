from win10toast import ToastNotifier
from datetime import datetime

def show_notification(title, message):
    toaster = ToastNotifier()
    toaster.show_toast(title, message, duration=2)




if __name__ == "__main__":

    with open('D:\\Notifier in Python\\task.txt') as f:
        task_file = f.read()
    task_file = task_file.split('-')
    task_time = task_file[2]
    task_time = float(task_time)
    now_time = datetime.now()
    now_time = float(now_time.timestamp())
    if task_time <= now_time:
        show_notification(task_file[0], task_file[1])
    else:
        pass