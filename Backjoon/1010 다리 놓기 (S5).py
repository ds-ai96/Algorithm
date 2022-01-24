"""
BAEKJOON ALGORITHM
Date : 2022-01-24
Start Time : 11:12
End Time : 11:37
File Name : 1010 다리 놓기 (S5)
URL : https://www.acmicpc.net/problem/1010
Category : Dynamic Programming
"""
def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    result = factorial(M) // (factorial(N) * factorial(M-N))
    print(result)