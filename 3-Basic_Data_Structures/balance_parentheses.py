#Balance Parentheses Checking

from stack import Stack

def par_checker(para):
  s = Stack()
  flag = True
  for i in para:
      if i == '(':
         s.push(i)
      elif i == ')':
         if  s.is_empty():
           flag = False
         else :
           flag = '(' == s.pop() 
      else :
         flag = False
  return s.is_empty() and flag


print(par_checker('((()))'))
print(par_checker(')'))
