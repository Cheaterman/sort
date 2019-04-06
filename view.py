import functools
import queue
import random
import threading
import time

from kivy.app import App
from kivy.clock import Clock, mainthread
from kivy.properties import ListProperty

# MONKEY PAAAATCH!!!
from qsort import pivot_choice

sort_queue = queue.Queue()

def swap(iterable, index_1, index_2):
    iterable[index_1], iterable[index_2] = (
        iterable[index_2], iterable[index_1]
    )
    sort_queue.put(iterable)
    time.sleep(SORT_DELAY)

def partition(iterable, start, end):
    pivot, original_pivot_index = pivot_choice(iterable, start, end)
    pivot_index = start

    for index in range(start, end + 1):
        if(
            index == original_pivot_index
            or iterable[index] > pivot
        ):
            continue

        swap(iterable, pivot_index, index)

        if pivot_index == original_pivot_index:
            original_pivot_index = index

        pivot_index += 1

    swap(iterable, pivot_index, original_pivot_index)

    return pivot_index

SORT_DELAY = .001

import qsort
qsort.partition = partition

from qsort import qsort


class View(App):
    dataset = ListProperty()

    def build(self):
        self.starting = False
        self.init()

    def init(self):
        self.starting = True
        Clock.schedule_once(self.start_sort, 1)

    def start_sort(self, *args):
        self.sorting_thread = sorting_thread = threading.Thread(
            target=qsort,
            args=([
                random.random()
                for i in range(500)
            ],),
            daemon=True,
        )
        sorting_thread.start()
        Clock.unschedule(self.update_sort)
        Clock.schedule_interval(self.update_sort, 0)
        self.starting = False

    def update_sort(self, *args):
        data = None

        while True:
            try:
                data = sort_queue.get_nowait()
            except queue.Empty:
                break

        if data is not None:
            self.dataset = data

        if not self.sorting_thread.is_alive() and not self.starting:
            self.init()


View().run()
