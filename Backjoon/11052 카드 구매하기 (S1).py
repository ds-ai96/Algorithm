"""
BAEKJOON ALGORITHM
Date : 2022-01-27
Start Time : 14:17
End Time : 14:32
File Name : 11052 카드 구매하기 (S1)
URL : https://www.acmicpc.net/problem/11052
Category : Dynamic Programming
"""

N = int(input())
P = [0] + list(map(int, input().split()))
dp = [0 for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + P[j])

print(dp[N])