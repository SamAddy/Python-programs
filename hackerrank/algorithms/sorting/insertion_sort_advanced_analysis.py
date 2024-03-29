"""
Insertion Sort is a simple sorting technique which was covered in previous challenges. Sometimes, arrays may be too large for us to wait around for insertion sort to finish. Is there some other way we can calculate the number of shifts an insertion sort performs when sorting an array?

If
is the number of elements over which the element of the array has to shift, then the total number of shifts will be ... +

.

Example

Array		Shifts
[4,3,2,1]
[3,4,2,1]	1
[2,3,4,1]	2
[1,2,3,4]	3

Total shifts = 1 + 2 + 3 = 6

Function description

Complete the insertionSort function in the editor below.

insertionSort has the following parameter(s):

    int arr[n]: an array of integers

Returns
- int: the number of shifts required to sort the array

Input Format

The first line contains a single integer

, the number of queries to perform.

The following

pairs of lines are as follows:

    The first line contains an integer

, the length of
.
The second line contains
space-separated integers

    .

Constraints

Sample Input

2
5
1 1 1 2 2
5
2 1 3 1 2

Sample Output

0
4

Explanation

The first query is already sorted, so there is no need to shift any elements. In the second case, it will proceed in the following way.

Array: 2 1 3 1 2 -> 1 2 3 1 2 -> 1 1 2 3 2 -> 1 1 2 2 3
Moves:   -        1       -    2         -  1            = 4
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def insertionSort(arr):
    def merge(left, right):
        shifts = 0
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                shifts += len(left) - i
        result.extend(left[i:])
        result.extend(right[j:])
        return result, shifts

    def mergeSort(arr):
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        left, left_shifts = mergeSort(arr[:mid])
        right, right_shifts = mergeSort(arr[mid:])
        sorted_arr, merge_shifts = merge(left, right)
        total_shifts = left_shifts + right_shifts + merge_shifts
        return sorted_arr, total_shifts

    _, shifts = mergeSort(arr)
    return shifts

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()