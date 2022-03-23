"""
BAEKJOON ALGORITHM
Date : 2022-03-23
Start Time : 14:21
End Time : 14:25
File Name : 2293 동전 1
URL : https://www.acmicpc.net/problem/2293
Category : Dynamic Programming
"""

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0 for _ in range(k+1)]
dp[0] = 1

for coin in coins:
    for idx in range(coin, k+1):
        if idx - coin >= 0:
            dp[idx] += dp[idx-coin]
        
print(dp[k]) 