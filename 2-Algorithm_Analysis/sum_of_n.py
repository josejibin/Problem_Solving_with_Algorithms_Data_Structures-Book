#sum of n numbers and using benchmark

import time
def sum_of_n(n):
  start = time.time()
  sum = 0
  for i in range(1, n+1):
    sum += i
  end = time.time()

  return sum,end-start

for i in range(5): 
   print "Sum is %d required %10.7f sec" % sum_of_n(100000)

