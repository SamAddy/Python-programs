"""
Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

One fine day, a finite number of tourists come to stay at the hotel.
The tourists consist of:
→ A Captain.
→ An unknown group of families consisting of K members per group where K ≠ 1

The Captain was given a separate room, and the rest were given one room per group.

Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all
the tourists. The room numbers will appear times per group except for the Captain's room.
Mr. Anant needs you to help him find the Captain's room number.
The total number of tourists or the total number of groups of families is not known to you.
You only know the value of

and the room number list.

Input Format

The first line consists of an integer, K, the size of each group.
The second line contains the unordered elements of the room number list.

Constraints
1 < K < 1000

Output Format
Output the Captain's room number.

Sample Input
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2

Sample Output
8

Explanation

The list of room numbers contains
elements. Since is , there must be groups of families. In the given list, all the numbers repeat
times except for room number .
Hence, 8 is the Captain's room number.
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    k = int(input())
    elements = list(map(int, input().split()))

    elements.sort()

    captain_room = None

    for i in range(0, len(elements), k):
        if i + k >= len(elements) or elements[i] != elements[i + k - 1]:
            captain_room = elements[i]
            break

    print(captain_room)
