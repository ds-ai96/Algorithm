"""
BAEKJOON ALGORITHM
Date : 2022-04-06
Start Time : 13:41
End Time : 14:26
File Name : 10986 나머지 합
URL : https://www.acmicpc.net/problem/10986
Category : Mathematics
"""
import sys

N, M = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))

psum = 0
cnt = [0] * M

for idx in range(N):
    psum = (psum + A[idx]) % M
    cnt[psum] += 1

print(cnt)

result = 0
for idx in range(M):
    if idx == 0:
        result += cnt[idx] * (cnt[idx] + 1) >> 1
        
    else:
        result += cnt[idx] * (cnt[idx] - 1) >> 1

print(result)        