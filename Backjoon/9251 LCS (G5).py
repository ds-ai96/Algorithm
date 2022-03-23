"""
BAEKJOON ALGORITHM
Date : 2022-03-23
Start Time : 15:04
End Time : 15:42
File Name : 9251 LCS 
URL : https://www.acmicpc.net/problem/9251
Category : Dynamic Programming
"""
import sys

String1 = list(sys.stdin.readline().rstrip())
String2 = list(sys.stdin.readline().rstrip())

dp = [[0] * (len(String1) + 1) for _ in range(len(String2) + 1)]

for s2_idx in range(1, len(String2) + 1):
    for s1_idx in range(1, len(String1) + 1):
        if String1[s1_idx - 1] == String2[s2_idx - 1]:
            dp[s2_idx][s1_idx] = dp[s2_idx - 1][s1_idx - 1] + 1
        else:
            dp[s2_idx][s1_idx] = max(dp[s2_idx - 1][s1_idx], dp[s2_idx][s1_idx - 1])
            
print(dp[-1][-1])