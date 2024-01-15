# This is a sample Python script.
#  im the best player alive
import random

x = int(random.uniform(1, 456 ))
y = int(random.uniform(1, 456 ))


if x > y:
   x = x - y
   print("now x is", x )
else:
    y = y - x
    print("now y is ", y )


