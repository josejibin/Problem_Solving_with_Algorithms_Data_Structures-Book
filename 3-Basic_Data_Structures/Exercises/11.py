#checking for balenced symbols

from stack import Stack
from queue import Queue

def html_tag_check():
  st = Stack()
  q = Queue()
  open_tag  , close_tag = "<", ">"
  with open('sample.html') as f:
    for s in f.read():
      if s != '':
         q.enqueue(s)
       

  print q
def main():
  html_tag_check()

if __name__ == "__main__":
  main()
