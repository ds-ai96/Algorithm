"""
BAEKJOON ALGORITHM
Date : 2022-03-28
Start Time : 14:24
End Time : 14:37
File Name : 1963 소수 경로 (G4)
URL : https://www.acmicpc.net/problem/1963
Category : Mathematics
"""
from collections import deque

# 4자리 소수 구하기
MAX = 9999
prime_number_idx = [True for _ in range(MAX + 1)] # 소수를 나타낼 행렬

for number in range(2, int(MAX ** 0.5)):
    if prime_number_idx:
        for idx in range(number+number, MAX+1, number):
            prime_number_idx[idx] = False
            
prime_number = [idx for idx, number in enumerate(prime_number_idx) if number == True and idx >= 1000]

def bfs():
    q = deque()
    q.append([A, 0])
    
    visited = [0 for _ in range(10000)]
    visited[A] = 1
    
    while q:
        now, cnt = q.popleft()
        string_now = str(now)
        
        if now == B:
            return cnt
        
        for i in range(4): # 1의 자리 ~ 1000의 자리
            for j in range(10): # 0 ~ 9
                tmp = int(string_now[:i] + str(j) + string_now[i+1:])
                
                if (visited[tmp] == 0) and (tmp in prime_number): # 방문 X & 1000~9999 구간의 소수인지 확인
                    visited[tmp] = 1
                    q.append([tmp, cnt+1])
                    
T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    result = bfs()
    print(result if result != None else "Impossible")