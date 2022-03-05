"""
BAEKJOON ALGORITHM
Date : 2022-03-05
Start Time : 14:56
End Time : 15:13
File Name : 9095 1, 2, 3 더하기
URL : https://www.acmicpc.net/problem/9095
Category : Bruteforcing
"""

T = int(input())
dp = [1, 2, 4] # n이 1, 2, 3인 경우

for i in range(3, 11):
    dp.append(dp[i-3] + dp[i-2] + dp[i-1])
    
for _ in range(T):
    n = int(input())   
    print(dp[n-1])