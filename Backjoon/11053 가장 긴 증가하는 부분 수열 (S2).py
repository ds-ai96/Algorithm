"""
BAEKJOON ALGORITHM
Date : 2022-04-16
Start Time : 15:15
End Time : 15:22
File Name : 11053 가장 긴 증가하는 부분 수열
URL : https://www.acmicpc.net/problem/11053
Category : Dynamic Programming
"""

A = int(input())
Array_A = list(map(int, input().split()))

LIS = [1 for _ in range(A)]

for i in range(A):
    for j in range(i):
        if Array_A[i] > Array_A[j]:
            LIS[i] = max(LIS[i], LIS[j]+1)
            
print(max(LIS))