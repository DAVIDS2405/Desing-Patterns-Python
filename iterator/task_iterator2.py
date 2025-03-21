from typing import List, Any
import time

class TaskList:
    def __init__(self, tasks: List[Any]):
        self.__tasks = tasks

    def __iter__(self):
        return TaskIterator(self)
    
    def get_tasks(self) -> List[Any]:
        return self.__tasks
    
class TaskIterator:
    def __init__(self, task_list: TaskList):
        self.task_list = task_list
        self.index = 0

    def __next__(self):
        if self.index < len(self.task_list.get_tasks()):
            task = self.task_list.get_tasks()[self.index]
            self.index += 1
            return task()
        else:
            raise StopIteration


def task1():
    return "Tarea 1 se ejecuta"

def task2():
    return "Tarea 2 se ejecuta"

def task3():
    return "Tarea 3 se ejecuta"

tasks = [task1, task2, task3]
task_list = TaskList(tasks)

for task in task_list:
    print(task)
    time.sleep(1)

for task in task_list:
    print(task)
    time.sleep(1)