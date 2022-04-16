"""
BAEKJOON ALGORITHM
Date : 2022-04-16
Start Time : 15:22
End Time : 15:27
File Name : 가장 큰 증가 부분 수열
URL : https://www.acmicpc.net/problem/11053
Category : Dynamic Programming
"""

N = int(input())
A = list(map(int, input().split()))

LISV = A.copy()

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            LISV[i] = max(LISV[i], LISV[j]+A[i])
            
print(max(LISV))