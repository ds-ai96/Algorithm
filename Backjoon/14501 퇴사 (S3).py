"""
BAEKJOON ALGORITHM
Date : 2021-12-30
Start Time : 14:16
End Time : 15:48
File Name : 14501 퇴사 (S3)
URL : https://www.acmicpc.net/problem/14501
Category : Bruteforcing
"""

N = int(input())
T, P = [0], [0]

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
    
result = [0 for _ in range(N+1)]

for i in range(1, N+1):
    result[i] = result[i-1]
    
    for j in range(1, i+1):
        if i - j + 1 == T[j]:
            result[i] = max(result[i], P[j] + result[j-1])
            
print(result[-1])