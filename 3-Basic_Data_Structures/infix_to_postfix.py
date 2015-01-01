#infix to postfix conversion

from stack import Stack


def inf_to_post(expr):
  pre = { "/" : 3, 
          "*" : 3,
          "+" : 2,
          "-" : 2,
          "(" : 1 }
  result = []
  s = Stack()
  exp = expr.split()
  for i in exp:
  #  print result,s
   
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
    

print(inf_to_post("A * B + C * D"))
print(inf_to_post("( A + B ) * C - ( D - E ) * ( F + G )"))
print inf_to_post("A + B")
