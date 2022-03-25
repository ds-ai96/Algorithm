"""
BAEKJOON ALGORITHM
Date : 2022-03-25
Start Time : 14:32
End Time : 14:54
File Name : 11054 가장 긴 바이토닉 부분 수열
URL : https://www.acmicpc.net/problem/11052
Category : Dynamic Programming
"""

N = int(input())

A = list(map(int, input().split()))

LIS = [ 1 for _ in range(N)] # Longest Increasing Subsequence 가장 긴 증가하는 부분수열
LDS = [ 1 for _ in range(N)] # Longest Decreasing Subsequence 가장 긴 감소하는 부분수열

# LIS 구하기
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            LIS[i] = max(LIS[i], LIS[j] + 1)

# LDS 구하기            
for i in range(N-1, -1, -1): # 뒤에서 부터 증가하는 수열 찾는 문제와 동일
    for j in range(N-1, i, -1):
        if A[i] > A[j]:
            LDS[i] = max(LDS[i], LDS[j]+1)
            
result = [0 for _ in range(N)]

for idx in range(N):
    result[idx] = LIS[idx] + LDS[idx] - 1 # 겹치는 부분 1 빼주기
    
print(max(result))