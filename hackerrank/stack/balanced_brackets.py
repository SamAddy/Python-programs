"""
A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].

Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a
closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of
brackets: [], {}, and ().

A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, {[(])} is
not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a single,
unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ].

By this logic, we say a sequence of brackets is balanced if the following conditions are met:

    It contains no unmatched brackets.
    The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.

Given

strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, return YES.
Otherwise, return NO.

Function Description

Complete the function isBalanced in the editor below.

isBalanced has the following parameter(s):

    string s: a string of brackets

Returns

    string: either YES or NO

Input Format

The first line contains a single integer
, the number of strings.
Each of the next lines contains a single string

, a sequence of brackets.

Constraints

, where

    is the length of the sequence.
    All chracters in the sequences ∈ { {, }, (, ), [, ] }.

Output Format

For each string, return YES or NO.

Sample Input

STDIN           Function
-----           --------
3               n = 3
{[()]}          first s = '{[()]}'
{[(])}          second s = '{[(])}'
{{[[(())]]}}    third s ='{{[[(())]]}}'

Sample Output

YES
NO
YES

Explanation

    The string {[()]} meets both criteria for being a balanced string.
    The string {[(])} is not balanced because the brackets enclosed by the matched pair { and } are not balanced: [(]).
    The string {{[[(())]]}} meets both criteria for being a balanced string.

"""

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here

    stack = []
    # A Hashmap for brackets
    bracket_pair = {
        '{': '}',
        '(': ')',
        '[': ']'
    }

    # Iterate through s
    for char in s:
        if char in bracket_pair:
            stack.append(char)
        else:
            if not stack:
                return 'NO'
            else:
                # Fetch last element in the stack
                opening_bracket = stack.pop()
                # Compare opening bracket to see if it matches its closing bracket
                if bracket_pair[opening_bracket] != char:
                    return 'NO'
    return 'YES' if not stack else 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
