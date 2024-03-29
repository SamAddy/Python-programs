"""
The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in
combination. Together, they form an iterator algebra making it possible to construct specialized tools succinctly
and efficiently in pure Python.

To read more about the functions in this module, check out their documentation here
(https://docs.python.org/2/library/itertools.html).

You are given a list of K lowercase English letters. For a given integer K, you can select any indices (assume 1
-based indexing) with a uniform probability from the list.

Find the probability that at least one of the indices selected will contain the letter: 'a'.

Input Format

The input consists of three lines. The first line contains the integer
, denoting the length of the list. The next line consists of

space-separated lowercase English letters, denoting the elements of the list.

The third and the last line of input contains the integer

, denoting the number of indices to be selected.

Output Format

Output a single line consisting of the probability that at least one of the
indices selected contains the letter:'

'.

Note: The answer must be correct up to 3 decimal places.

Constraints

All the letters in the list are lowercase English letters.

Sample Input

4
a a c d
2

Sample Output

0.8333

Explanation

All possible unordered tuples of length
comprising of indices from to

are:

Out of these 6 combinations, 5 of them contain either index or index which are the indices that contain the letter '

'.
Hence, the answer is
.
"""

from itertools import combinations

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = input().replace(" ", "")
r = int(input())

combs_count_with_a = len(list(filter(lambda x: 'a' in x, combinations(s, r))))

probability_of_a = combs_count_with_a / len(list(combinations(s, r)))
print(f"{probability_of_a:.3f}")
