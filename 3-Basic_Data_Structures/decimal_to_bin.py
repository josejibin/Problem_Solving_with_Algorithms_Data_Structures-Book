#convart decimal numbers to binary using stack

from stack import Stack

def divide_by2(num):
  s = Stack()
  while num > 0:
    if num % 2:
       s.push(1)
    else :
       s.push(0)
    num /= 2
  to_bin(s)

def to_bin(s):
 bin = ''
 while not s.is_empty():
   bin += str(s.pop())
 print bin

divide_by2(233) 

