"""
BAEKJOON ALGORITHM
Date : 2022-03-03
Start Time : 14:45
End Time : 14:57
File Name : 1476 날짜 계산 (S5)
URL : https://www.acmicpc.net/problem/1476
Category : Bruteforcing
"""
import sys

Year = list(map(int, sys.stdin.readline().split()))

E = 0 # 1 <= E <= 15
S = 0 # 1 <= S <= 28
M = 0 # 1 <= M <= 19

cnt = 0

while True:    
    if (E == Year[0]) and (S == Year[1]) and (M == Year[2]): break # 종료 조건
    
    # 1년씩 더하면서 모든 경우 점검
    E += 1
    S += 1
    M += 1
    cnt += 1
    if E > 15: E -= 15
    if S > 28: S -= 28
    if M > 19: M -= 19
    
print(cnt)