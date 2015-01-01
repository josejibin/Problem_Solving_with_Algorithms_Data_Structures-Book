#a direct infix evaluator

from stack import Stack

def inf_to_post(expr):
  pre = { "/" : 3, 
          "*" : 3,
          "+" : 2,
          "-" : 2,
          "(" : 1 }
  result = []
  s = Stack()
  exp = list(expr)
  for i in exp:
    if i.isalpha() or i.isdigit() :
      result.append(i)
    elif i == '(' :
      s.push(i)
    elif i == ')':
      top_token = s.pop()
      while top_token != '(':
         result.append(top_token)
         top_token = s.pop()
    else :
     
      while (not s.is_empty())  and (pre[s.peek()] >= pre[i]) :
       # print pre[s.peek()],pre[i]
        result.append(s.pop())
      s.push(i)
  while not s.is_empty():
     result.append(s.pop())
  return "".join(result)

def postfix_eval(expr):
  s = Stack()
  exp = list(expr)
  for i in exp:
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


def infix_eval():
  expr = raw_input("Enter an infix expression :")
  postfix = inf_to_post(expr)
  result = postfix_eval(postfix)
  print expr + " = " +str(result) 

def main():
  infix_eval()

if __name__ == "__main__":
    main()
