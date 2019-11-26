import time
from multiprocessing import JoinableQueue, Queue, Process, current_process

# execute the command and check python process via `ps -ef | grep python` command


class Task:
    def __init__(self, message_queue: Queue):
        self.message_queue = message_queue

    def run(self):
        start_time = time.time()
        while time.time() - start_time < 60:
            name = current_process().name
            try:
                message = self.message_queue.get_nowait()
                self.message_queue.task_done()
                time.sleep(2) # 2 seconds to process the message
                print(f'{name}: {message}')
            except Exception as ex:
                print(f'{name}: No messages' + str(ex))
            time.sleep(1)


def run_task(message_queue: Queue):
    task = Task(message_queue)
    task.run()


if __name__ == '__main__':
    message_queue = JoinableQueue()
    for i in range(1, 20):
        p = Process(name=f'Task {i}', target=run_task, args=(message_queue,))
        p.start()

    for i in range(1, 2000):
        message_queue.put(f'hello {i}')
        print('Enqueuing message: ' + str(i))
