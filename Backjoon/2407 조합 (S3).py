"""
BAEKJOON ALGORITHM
Date : 2022-03-19
Start Time : 14:35
End Time : 14:50
File Name : 2407 조합 (S3)
URL : https://www.acmicpc.net/problem/2407
Category : Mathematics
"""

import sys
from functools import reduce

n, m = map(int, sys.stdin.readline().split())

def nCm(n, m):
    m = min(m, n-m) # nCm == nC(c-m)
    bunja = reduce(lambda x, y: x*y, range(n, n-m, -1), 1) # n부터 n-m+1까지의 팩토리얼
    bunmo = reduce(lambda x, y: x*y, range(1, m+1, 1), 1) # 1부터 r까지의 팩토리얼
    return bunja // bunmo

print(nCm(n, m))