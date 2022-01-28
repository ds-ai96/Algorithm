"""
BAEKJOON ALGORITHM
Date : 2022-01-28
Start Time : 11:35
End Time : 12:18
File Name : 12865 평범한 배낭 (G5)
URL : https://www.acmicpc.net/problem/12865
Category : Dynamic Programming
"""

N, K = map(int, input().split())
M = [[0, 0]]
for _ in range(N):
    w, v = map(int, input().split())
    M.append([w, v])
    
M.sort()

dp = [[0] * (K+1) for _ in range(N+1)]

for n in range(1, N+1):
    for w in range(1, K+1):
        weight = M[n][0]
        value = M[n][1]
        
        if w < weight:
            dp[n][w] = dp[n-1][w]
        else:
            dp[n][w] = max(dp[n-1][w], value + dp[n-1][w-weight])
        
print(dp[N][K])