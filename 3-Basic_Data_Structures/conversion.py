# convert decimal num to binary,octel,hexadecimal

from stack import Stack

def base_converter(num,base):
  digits = "0123456789ABCDEF"
  s = Stack()

  while num > 0:
    s.push(num % base)
    num //= base

  result = ""
  while not s.is_empty():
    result += digits[s.pop()]
  return result

print (base_converter(25,2))
print (base_converter(25,16))
print (base_converter(255,16))
print (base_converter(255,8))
