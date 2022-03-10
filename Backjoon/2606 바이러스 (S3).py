"""
BAEKJOON ALGORITHM
Date : 2022-03-10
Start Time : 14:55
End Time : 15:01
File Name : 2606 바이러스 (S3)
URL : https://www.acmicpc.net/problem/2606
Category : DFS & BFS
"""
import sys
from collections import deque

def BFS(graph, Start_V = 1):
    cnt = 0
    went = [Start_V]
    
    path = deque()
    path.append(Start_V)
    
    while path:
        go_to_v = path.popleft()
        
        
        for next in range(len(graph[Start_V])):
            if (graph[go_to_v][next] == 1) and (next not in went):
                cnt += 1
                went.append(next)
                path.append(next)
        
    print(cnt)

N = int(sys.stdin.readline())
E = int(sys.stdin.readline())

graph = [ [0] * (N + 1) for _ in range(N + 1)]

for _ in range(E):
    e1, e2 = map(int, sys.stdin.readline().split())
    graph[e1][e2] = graph[e2][e1] = 1
    
BFS(graph, 1)