"""
BAEKJOON ALGORITHM
Date : 2022-02-17
Start Time : 17:59
End Time : 18:09
File Name : 6588 골드바흐의 추측 (S1)
URL : https://www.acmicpc.net/problem/6588
Category : Mathematics
"""
import sys

sosu_list = [True for _ in range(1000001)]

for i in range(2, 1001):
    if sosu_list[i]:
        for j in range(i + i, 1000001, i):
            sosu_list[j] = False
            
while True:
    n = int(sys.stdin.readline())
    
    if n == 0: break
    
    for i in range(3, len(sosu_list)):
        if sosu_list[i] and sosu_list[n-i]:
            print(n, "=", i, "+", n-i)
            break