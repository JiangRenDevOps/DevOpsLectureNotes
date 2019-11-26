import time
from multiprocessing import Process
from queue import Queue
from threading import Thread


class Task:
    def __init__(self, message_queue: Queue):
        self.message_queue = message_queue

    def run(self):
        start_time = time.time()
        while time.time() - start_time < 60:
            try:
                message = self.message_queue.get_nowait()
                print(message)
                self.message_queue.task_done()
            except Exception:
                print("No messages")
            time.sleep(1)


def run_task(message_queue: Queue):
    task = Task(message_queue)
    task.run()


if __name__ == '__main__':
    message_queue = Queue()
    p = Process(target=run_task, args=(message_queue,))
    # p = Thread(target=run_task, args=(message_queue,))
    p.start()
    time.sleep(5)
    message_queue.put("hello")
