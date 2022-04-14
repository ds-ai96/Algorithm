"""
BAEKJOON ALGORITHM
Date : 2022-04-14
Start Time : 14:01
End Time : 14:24
File Name : 2143 두 배열의 합 (G3)
URL : https://www.acmicpc.net/problem/2143
Category : Binary Search
"""
from collections import defaultdict

T = int(input())

A = int(input())
Array_A = list(map(int, input().split()))

B = int(input())
Array_B = list(map(int, input().split()))

dictA = defaultdict(int)

for i in range(A):
    for j in range(i, A):
        dictA[sum(Array_A[i:j+1])] += 1
        
result = 0

for i in range(B):
    for j in range(i, B):
        result += dictA[T - sum(Array_B[i:j+1])]
        
print(result)