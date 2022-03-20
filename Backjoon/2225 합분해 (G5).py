"""
BAEKJOON ALGORITHM
Date : 2022-03-20
Start Time : 17:39
End Time : 17:54
File Name : 2225 합분해 (G5)
URL : https://www.acmicpc.net/problem/2225
Category : Mathematics
"""
import sys

N, K = map(int, sys.stdin.readline().split())

dp = [[0] * 201 for _ in range(201)] # N, K 의 최댓값 200개 + 0번 index

for idx in range(201):
    dp[1][idx] = 1
    
for i in range(2, 201):
    dp[i][1] = i
    for j in range(2, 201):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 1000000000

print(dp[K][N])