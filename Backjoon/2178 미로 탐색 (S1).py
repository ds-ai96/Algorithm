"""
BAEKJOON ALGORITHM
Date : 2022-01-10
Start Time : 
End Time : 
File Name : 2178 미로 탐색 (S1)
URL : https://www.acmicpc.net/problem/2178
Category : DFS & BFS
"""

from collections import deque

        
N, M = map(int, input().split())

Miro = [[0 for i in range(M+1)]]
for _ in range(N):
    Miro.append([0] + list(map(int, input())))

