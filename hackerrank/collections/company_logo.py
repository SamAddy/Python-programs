""""
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string

, which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

    Print the three most common characters along with their occurrence count.
    Sort in descending order of occurrence count.
    If the occurrence count is the same, sort the characters in alphabetical order.

For example, according to the conditions described above,

would have it's logo with the letters

.

Input Format

A single line of input containing the string

.

Constraints

has at least

    distinct characters

Output Format

Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.

Sample Input 0

aabbbccde

Sample Output 0

b 3
a 2
c 2

"""
from collections import Counter

if __name__ == '__main__':
    s = input()
    letters_count = {}
    for letter in sorted(set(s)):
        letters_count[letter] = s.count(letter)

    sorted_dict = dict(sorted(letters_count.items(), key=lambda item: item[1], reverse=True)[:3])

    for i, e in enumerate(sorted_dict):
        print(e, letters_count[e])

# Or

if __name__ == '__main__':
    s = input()
    letters_count = Counter(s)
    for k, v in letters_count.most_common(3):
        print(k, v)
