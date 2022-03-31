"""
BAEKJOON ALGORITHM
Date : 2022-03-31
Start Time : 14:58
End Time : 15:33
File Name : 11049 행렬 곱셈 순서 (G3)
URL : https://www.acmicpc.net/problem/11049
Category : Dynamic Programming
"""

MAX = 2 ** 31 - 1
N = int(input())

R = []
C = []

RC = [list(map(int, input().split())) for _ in range(N)]    
dp = [[0] * N for _ in range(N)]

for size in range(1, N): # 부분 문제의 크기
    for i in range(N-size):
        j = i + size
        dp[i][j] = MAX
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + RC[i][0] * RC[k][1] * RC[j][1])
            
print(dp[0][-1])