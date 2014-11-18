#find the minimum number in a list with O(n^2)

import time

def find_min(n,l):
  start = time.time()
  for i in l:
    if n == i:
      end = time.time()
      return start-end


for i in range(5): 
   print "required %10.7f sec" % find_min('a',['w','w','w','w','w','b','c','d','e','a'])
  
