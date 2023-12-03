#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxLength' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#A subarray of array a is defined as a contiguous block of a's elements having a length that is less than or equal to the length of
# the array. For example, the subarrays of array a = [1, 2, 3] are [1], [2], [3], [1, 2], [2, 3], and [1, 2, 3]. Given an integer, k = 3, the
# subarrays having elements that sum to a number ≤ k are [1], [2], and [1, 2]. The longest of these subarrays is [1, 2], which has a
# length of 2. Given an array, a, determine its longest subarray that sums to less than or equal to a given value k.
# Function Description
# Complete the function maxLength in the editor below. The function must return an integer that represents the length of the
# longest subarray of a that sums to a number ≤ k.
# maxLength has the following parameter(s):
# a[a[0],...a[n-1]]: an array of integers

def maxLength(a, k):
    n = len(a)
    max_length = 0
    current_sum = 0
    start = 0

    for end in range(n):
        current_sum += a[end]

        while current_sum > k:
            current_sum -= a[start]
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    k = int(input().strip())

    result = maxLength(a, k)

    fptr.write(str(result) + '\n')

    fptr.close()
