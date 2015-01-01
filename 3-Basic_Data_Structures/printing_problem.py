#printing problem implementation

from queue import Queue
from printer import Printer
from task import Task

import random

def simulation(num_seconds, pages_per_minute):
  lab_printer = Printer(pages_per_minute)
  print_queue = Queue()
  waiting_time = []

