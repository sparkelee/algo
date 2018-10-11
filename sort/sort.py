#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math

n = 2
while True:
    a = 8*n*n
    b = 8*n*math.log2(n)
    if a >= b:
        print(n, a, b)
        break
    n += 1

# n = 1
# while True:
#     if 100*n*n < 2**n:
#         print(n, 100*n*n, 2**n)
#         break
#     n += 1


# def calc_n(ms):
#     # lg(n)
#     # print(2**ms)
#     # sqrt(n)
#     print(ms*ms)
#     # n
#     print(ms)
#     # nlgn
#     for i in range(ms, int(math.sqrt(ms))):
#         if i*math.log2(i) >= ms:
#             print(i-1)
#             break
#     # n * n
#     print(math.sqrt(ms))
#     # n * n * n
#     print(math.pow(ms, 1/3))
#     # 2**n
#     print(math.log2(ms))
#     # n!
#     for i in range(1, int(math.log2(ms))):
#         if math.factorial(i) >= ms:
#             print(i-1)
#             break


# calc_n(1000*60*60*24*365*100)

# print(math.factorial(15))


import numpy as np
import time
unsort_list = np.random.rand(100)


def insert_sort(s):
    cyc = 0
    start_ts = time.time()
    i = 1
    while i < len(s):
        j = i-1
        key = s[i]
        while (j >= 0) and (s[j] < key):
            s[j+1] = s[j]
            j -= 1
            cyc += 1
        s[j+1] = key
        i += 1
    end_ts = time.time()
    print(cyc, end_ts - start_ts)


# print(unsort_list)
insert_sort(unsort_list)
print(unsort_list)
