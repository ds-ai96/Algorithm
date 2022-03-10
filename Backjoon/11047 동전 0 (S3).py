"""
BAEKJOON ALGORITHM
Date : 2022-03-10
Start Time : 15:03
End Time : 15:10
File Name : 11047 동전 0 (S3)
URL : https://www.acmicpc.net/problem/11047
Category : Greedy
"""
import sys

N, K = map(int, sys.stdin.readline().split())

coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline()))
    
cnt = 0

for coin in coins[::-1]:
    cnt += (K // coin)
    K %= coin
            
print(cnt)