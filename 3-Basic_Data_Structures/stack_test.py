#for testing stack implementation

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
