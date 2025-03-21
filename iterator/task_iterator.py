from abc import ABC, abstractmethod
from typing import Any, List
import time

class Iterator(ABC):
    @abstractmethod
    def next(self) -> Any:
        pass

    @abstractmethod
    def has_next(self) -> bool:
        pass

class IterableCollection(ABC):
    @abstractmethod
    def create_iterator(self) -> Iterator:
        pass

class TaskList(IterableCollection):
    def __init__(self, tasks: List[Any]):
        self.__tasks = tasks

    def create_iterator(self):
        return TaskIterator(self)
    
    def get_tasks(self) -> List[Any]:
        return self.__tasks
    
class TaskIterator(Iterator):
    def __init__(self,  task_list: TaskList):
        self.task_list = task_list
        self.index = 0

    def has_next(self) -> bool:
        return self.index < len(self.task_list.get_tasks())
    
    def next(self) -> Any:
        if self.has_next():
            task = self.task_list.get_tasks()[self.index]
            self.index += 1
            return task()
        

def task1():
        return "Tarea 1 se ejecuta"

def task2():
        return "Tarea 2 se ejecuta"

def task3():
        return "Tarea 3 se ejecuta"

tasks = [task1, task2, task3]
task_list = TaskList(tasks)
task_iterator = task_list.create_iterator()

while task_iterator.has_next():
     print(task_iterator.next())
     time.sleep(3)