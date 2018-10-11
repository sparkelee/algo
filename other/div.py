#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math
import numpy as np
import time


def find_max_crossing_subarray(arr, low, mid, high):
    max_left_sum = float('-Inf')
    max_right_sum = float('-Inf')
    i = mid
    j = mid+1
    max_left = -1
    max_right = -1
    left_sum = 0
    right_sum = 0
    while i >= low:
        left_sum += arr[i]
        if left_sum > max_left_sum:
            max_left_sum = left_sum
            max_left = i
        i -= 1
    while j <= high:
        right_sum += arr[j]
        if right_sum > max_right_sum:
            max_right_sum = right_sum
            max_right = j
        j += 1
    return (max_left, max_right, max_left_sum + max_right_sum)


def find_max_subarray(arr, low, high):
    if low == high:
        return (low, high, arr[low])
    mid = int((high+low)/2)
    (left_l, left_r, left_sum) = find_max_subarray(arr, low, mid)
    (right_l, right_r, right_sum) = find_max_subarray(arr, mid+1, high)
    (cross_l, cross_r, cross_sum) = find_max_crossing_subarray(arr, low, mid, high)
    print('left: ', left_l, left_r, left_sum)
    print('right: ', right_l, right_r, right_sum)
    print('cross: ', cross_l, cross_r, cross_sum)
    if (left_sum >= right_sum) and (left_sum >= cross_sum):
        return (left_l, left_r, left_sum)
    elif (right_sum >= left_sum) and (right_sum >= cross_sum):
        return (right_l, right_r, right_sum)
    else:
        return (cross_l, cross_r, cross_sum)


def test_find_max_subarray():
    arr_len = 10
    arr = np.random.randint(-1000, 1000, arr_len)
    print(arr)
    ret = find_max_subarray(arr, 0, len(arr)-1)
    print(ret)

# n*n matrix


def matrix_multi(a, b):
    n = len(a)
    c = a
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    return c

# n/2 == 0


def matrix_mutli_recursive(a, b):
    pass


def test_matrix_multi():
    a = np.random.rand(2, 2)
    b = np.random.rand(2, 2)
    print(a, '\n')
    print(b, '\n')
    c = matrix_multi(a, b)
    print(c)


def ts_36trans10(num):
    # 1az
    base = '0123456789abcdefghijklmnopqrstuvwxyz'
    res = 0
    for i in range(len(num)):
        idx = base.find(num[i])
        res += idx * pow(36, len(num)-i-1)
    return res


def ts_10trans36(num):
    base = '0123456789abcdefghijklmnopqrstuvwxyz'
    res = ''
    if num == 0:
        return "0"
    while num > 0:
        res = base[num % 36] + res
        num = num/36
    return res


if __name__ == '__main__':
    # test_find_max_subarray()
    # test_matrix_multi()
    print(ts_10trans36(71))
