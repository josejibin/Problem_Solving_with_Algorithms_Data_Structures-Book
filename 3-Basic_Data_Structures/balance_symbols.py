#checking for balenced symbols

from stack import Stack

def sym_check(sym):
  st = Stack()
  push_sym, pop_sym = "{[(<", "}])>"
  for s in sym:
   # print s
    
    if s in push_sym:
      st.push(s)
      print st
    elif s in pop_sym:
      if st.is_empty():
        return False
      else:
        poped = st.pop()
        desired_sym = push_sym[pop_sym.index(s)]
       # print poped,desired_sym
        if poped != desired_sym:
           return False
    else:
        return False
  return st.is_empty()


print(sym_check('{{([][])}()}'))
print(sym_check('[{()]'))
