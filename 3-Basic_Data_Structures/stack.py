#Stack implementation usinfg list

class Stack():
 def __init__(self):
    self.items = []

 def push(self,item):
    self.items.append(item)

 def pop(self):
    return self.items.pop()

 def peek(self):
    return self.items[len(self.items)-1]

 def is_empty(self):
    return not self.items

 def size(self):
    return len(self.items)

 def __str__(self):
    return "stack is "+str(self.items)

a = Stack()
print a
a.push(4)
a.push(5)
a.push(2)
print a
print a.peek()
a.pop()
print a
print a.is_empty()
print a.peek()
a.pop()
a.pop() 
print a
print a.is_empty()

m = Stack()
m.push('x')
m.push('y')
m.push('z')
while not m.is_empty():
  m.pop()
  m.pop()
print m
