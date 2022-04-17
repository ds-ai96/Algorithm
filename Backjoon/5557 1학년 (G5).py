"""
BAEKJOON ALGORITHM
Date : 2022-04-17
Start Time : 21:10
End Time : 21:24
File Name : 5557 1학년
URL : https://www.acmicpc.net/problem/5557
Category : Dynamic Programming
"""
N = int(input())
Array_N = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(N)]
dp[0][Array_N[0]] = 1

for i in range(N-1):
    for j in range(21):
        if dp[i][j] != 0:
            if 0 <= j + Array_N[i+1] <= 20: dp[i+1][j + Array_N[i+1]] += dp[i][j]
            if 0 <= j - Array_N[i+1] <= 20: dp[i+1][j - Array_N[i+1]] += dp[i][j]
        
print(dp[-2][Array_N[-1]])