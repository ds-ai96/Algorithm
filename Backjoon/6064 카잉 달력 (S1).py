"""
BAEKJOON ALGORITHM
Date : 2022-03-05
Start Time : 15:19
End Time : 15:43
File Name : 6064 카잉 달력 (S1)
URL : https://www.acmicpc.net/problem/6064
Category : Bruteforcing
"""

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    p = 1
    while (x <= M*N):
        if (x % N) == (y % N):
            print(x)
            p = 0
            break
        x += M
        
    if p == 1:
        print(-1)