import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        with open("./calculations.txt", 'r') as file:
            print(file.readlines()[-1])


event_handler = Handler()
observer = Observer()
observer.schedule(event_handler, path="./", recursive=True)
observer.start()
while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
