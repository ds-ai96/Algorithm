"""
BAEKJOON ALGORITHM
Date : 2022-01-13
Start Time : 13:13
End Time : 13:56
File Name : 1461 도서관 (G5)
URL : https://www.acmicpc.net/problem/1461
Category : Sorting
"""

N, M = map(int, input().split())
Book = list(map(int, input().split()))

pos_Book = [x for x in Book if x > 0]
neg_Book = [x for x in Book if x < 0]

pos_Book.sort(reverse=True)
neg_Book.sort()

pos_reach = pos_Book[::M]
neg_reach = list(map(lambda x: x*(-1), neg_Book[::M]))

reach = pos_reach + neg_reach
reach.sort(reverse=True)

result = 0
for i in reach:
    result += i*2

print(result - reach[0])
