import math
from math import sqrt
import time

start = time.time()

for i in range(100000000):
    sqrt(i)

print(time.time() - start)
