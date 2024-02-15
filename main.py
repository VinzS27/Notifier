from win10toast import ToastNotifier
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import ctypes
import os
import win32process

#chiudi console all'avvio
hwnd = ctypes.windll.kernel32.GetConsoleWindow()
if hwnd != 0:
    ctypes.windll.user32.ShowWindow(hwnd, 0)
    ctypes.windll.kernel32.CloseHandle(hwnd)
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    os.system('taskkill /PID ' + str(pid) + ' /f')

#------------------------

toast = ToastNotifier()
def on_created(event):
    toast.show_toast(
        "SalvaBarcode",
        "E' stato creato un nuovo file.",
        duration=20,
        icon_path="C:/Uploads/notification.ico",
        threaded=True,
    )
def on_deleted(event):
    toast.show_toast(
        "SalvaBarcode",
        "E' stato cancellato un file.",
        duration=20,
        icon_path="C:/Uploads/notification.ico",
        threaded=True,
    )
def on_modified(event):
    toast.show_toast(
        "SalvaBarcode",
        "E' stato modificato un file.",
        duration=20,
        icon_path="C:/Uploads/notification.ico",
        threaded=True,
    )
def on_moved(event):
    toast.show_toast(
        "SalvaBarcode",
        "E' stato spostato un file.",
        duration=20,
        icon_path="C:/Uploads/notification.ico",
        threaded=True,
    )


if __name__ == "__main__":

    event_handler = FileSystemEventHandler()

    event_handler.on_created = on_created
    event_handler.on_deleted = on_deleted
    event_handler.on_modified = on_modified
    event_handler.on_moved = on_moved

    path = "C:/Uploads"
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        #print("Monitoring")
        while True:
            time.sleep(3)
    except KeyboardInterrupt:
        observer.stop()
        #print("Done")
    observer.join()

