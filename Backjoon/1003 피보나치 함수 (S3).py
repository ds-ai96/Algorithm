"""
BAEKJOON ALGORITHM
Date : 2022-03-09
Start Time : 14:26
End Time : 14:36
File Name : 1003 피보나치 함수 (S3)
URL : https://www.acmicpc.net/problem/1003
Category : Dynamic Programming
"""
import sys

dp_f0 = [0] * 41
dp_f1 = [0] * 41

dp_f0[0] = 1
dp_f1[1] = 1

for idx in range(2, len(dp_f0)):
    dp_f0[idx] = dp_f0[idx-2] + dp_f0[idx-1]
    dp_f1[idx] = dp_f1[idx-2] + dp_f1[idx-1]
    
T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    print(dp_f0[N], dp_f1[N])