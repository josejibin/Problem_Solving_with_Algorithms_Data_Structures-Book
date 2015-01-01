#palidrome checking using deque

from deque import Deque

def is_palindrome(s):
  
  q = Deque()
  flag = True
  for char in s:
    q.add_front(char)
  print q
  for i in range((len(s)/2)-1):
     if   q.remove_front() != q.remove_rear():
       return False
  return flag




print is_palindrome("abba")
print is_palindrome("aba")
print is_palindrome("abcd")
print is_palindrome("malayalam")
