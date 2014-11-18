#sum of n umbers using equation

import time

def sum2(n):
  #start = time.time()
  s = (n*(n+1))/2
  #end = time.time()
  return s#,end-start



#for i in range(5): 
 #  print "Sum is %d required %10.7f sec" % sum2(100000)

import timeit
print(timeit.timeit("sum2(10000)", setup="from __main__ import sum2"))

