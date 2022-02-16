"""
BAEKJOON ALGORITHM
Date : 2022-02-16
Start Time : 16:36
End Time : 17:09
File Name : 17425 약수의 합 (G5)
URL : https://www.acmicpc.net/problem/17425
Category : Mathematics
"""

import sys
MAX = 1000000

# F == f(x) : 자연수 x의 약수의 합
F = [1] * (MAX+1)

# G == g(x) : x 보다 작거나 같은 모든 자연수 y의 f(y) 값을 더한 값
G = [0] * (MAX+1)

for num in range(2, MAX+1):
    mul = 1
    while num * mul <= MAX:
        F[num * mul] += num
        mul += 1
        
for idx in range(1, MAX+1):
    G[idx] = G[idx-1] + F[idx]

T = int(sys.stdin.readline()) # Task Case 입력
result = []

for _ in range(T):
    N = int(sys.stdin.readline())
    result.append(G[N])

print("\n".join(map(str, result)))