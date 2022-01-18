"""
BAEKJOON ALGORITHM
Date : 2022-01-11
Start Time : 14:16
End Time : 15:40 
File Name : 1174 줄어드는 수 (S1)
URL : https://www.acmicpc.net/problem/1174
Category : Sorting
"""

from itertools import combinations

N = int(input())

result = []

for num_len in range(1, 11):
    for num in combinations(range(0, 10), num_len):
        num = list(num)
        num.sort(reverse=True)
        result.append(int("".join(map(str, num))))
result.sort()

if len(result) >= N:
    print(result[N-1])
else:
    print(-1)