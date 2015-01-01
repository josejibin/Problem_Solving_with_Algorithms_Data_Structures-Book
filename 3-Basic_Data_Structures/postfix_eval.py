#postfix evaluation using stack

from stack import Stack

def postfix_eval(expr):
  s = Stack()
  exp = expr.split()
  for i in exp:
    print s
    if i.isdigit():
       s.push(int(i))
    else:
       s.push(do_math(s.pop(), s.pop(), i))
  return s.pop()

def do_math(b,a,op):
  if op == '+':
     return a + b
  elif op == '-':
     return a - b
  elif op == '/':
     return a / b
  else :
     return a * b


print postfix_eval('3 2 * 5 4 * +')
print postfix_eval('7 8 + 3 2 + /')
