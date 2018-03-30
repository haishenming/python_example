from random import random

import time

size = 100000

needles = (random() for i in range(10000))

super_dict = {i: random() for i in range(size)}
super_list = [random() for i in range(size)]
super_set = {random() for i in range(size)}
super_tuple = (random() for i in range(size))

print("Start {}".format(size))

print("Start dict {}".format(size))
start = time.time()
found = 0
for n in needles:
    if n in super_dict:
        found += 1
print("{}-{}".format(found, time.time() - start))

print("Start list {}".format(size))
start = time.time()
found = 0
for n in needles:
    if n in super_list:
        found += 1
print("{}-{}".format(found, time.time() - start))

print("Start set {}".format(size))
start = time.time()
found = 0
for n in needles:
    if n in super_set:
        found += 1
print("{}-{}".format(found, time.time() - start))

print("Start tuple {}".format(size))
start = time.time()
found = 0
for n in needles:
    if n in super_tuple:
        found += 1
print("{}-{}".format(found, time.time() - start))
