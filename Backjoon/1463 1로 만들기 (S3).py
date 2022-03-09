"""
BAEKJOON ALGORITHM
Date : 2022-03-09
Start Time : 14:37
End Time : 14:45
File Name : 1463 1로 만들기 (S3)
URL : https://www.acmicpc.net/problem/1463
Category : Dynamic Programming
"""

import sys

N = int(sys.stdin.readline())
dp = [0] * (N + 1)

for idx in range(2, N + 1):
    dp[idx] = dp[idx - 1] + 1
    if idx % 3 == 0:
        dp[idx] = min(dp[idx], dp[idx // 3] + 1)
    if idx % 2 == 0:
        dp[idx] = min(dp[idx], dp[idx // 2] + 1)
        
print(dp[N])