"""
BAEKJOON ALGORITHM
Date : 2022-01-26
Start Time : 14:03
End Time : 14:27
File Name : 14494 다이나믹이 뭐예요? (S2)
URL : https://www.acmicpc.net/problem/14494
Category : Dynamic Programming
"""

i, j = map(int, input().split())

dp = [[0] * (j+1) for _ in range(i+1)] # 시작 좌표를 (1,1)로 설정하기 위해서 padding 실시

for x in range(1, i+1): # 1열을 전부 1로 초기화
    dp[x][1] = 1
    
for y in range(1, j+1): # 1행을 전부 1로 초기화
    dp[1][y] = 1
    
for x in range(2, i+1):
    for y in range(2, j+1):
        dp[x][y] = dp[x-1][y-1] + dp[x-1][y] + dp[x][y-1]

print(dp[i][j] % 1000000007)