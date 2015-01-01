#Stack implementation usinfg list

class Stack():
 def __init__(self):
    self.items = []

 def push(self,item):
    self.items.append(item)

 def pop(self):
    return self.items.pop()

 def peek(self):
    if self.is_empty():
       return None
    else :
       return self.items[len(self.items)-1]

 def is_empty(self):
    return not self.items

 def size(self):
    return len(self.items)

 def __str__(self):
    return "stack is "+str(self.items)



