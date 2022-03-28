"""
BAEKJOON ALGORITHM
Date : 2022-03-28
Start Time : 14:38
End Time : 15:01
File Name : 14002 가장 긴 증가하는 부분 수열 4
URL : https://www.acmicpc.net/problem/14002
Category : Dynamic Programming
"""

N = int(input())

A = list(map(int, input().split()))

LIS = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            LIS[i] = max(LIS[i], LIS[j]+1)

result = max(LIS)
print(result)

LIS_list = []

for i in range(N-1, -1, -1):
    if LIS[i] == result:
        LIS_list.append(A[i])
        result -= 1
        
LIS_list.reverse()
print(*LIS_list)