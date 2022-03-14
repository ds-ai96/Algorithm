"""
BAEKJOON ALGORITHM
Date : 2022-03-14
Start Time : 11:06
End Time : 11:34
File Name : 6603 로또 (S2)
URL : https://www.acmicpc.net/problem/6603
Category : 	Recursion
"""
import sys
from itertools import combinations

while True:
    k, *S = map(int, sys.stdin.readline().split())
    if k == 0: break # 종료 조건 (0을 입력받으면 종료한다.)
    S = list(combinations(S, 6))
    for i in S:
        for j in i:
            print(j, end=" ")
        print()
    print()