"""
BAEKJOON ALGORITHM
Date : 2022-01-06
Start Time : 15:41
End Time : 16:21
File Name : 1260 DFS와 BFS (S2)
URL : https://www.acmicpc.net/problem/1260
Category : DFS & BFS
"""
from collections import deque

def DFS(graph, Start_V, went=[]):
    
    went.append(Start_V)
    print(Start_V, end=" ")
    
    for next in range(len(graph[Start_V])):
        if (graph[Start_V][next] == 1) and (next not in went):
            DFS(graph, next)
        

def BFS(graph, Start_V):
    
    went = [Start_V] # 방문했던 노드들
    
    path = deque() # 방문했던 순서
    path.append(Start_V)
    
    while path:
        
        go_to_v = path.popleft() # 다음으로 방문해야 하는 노드들
        print(go_to_v, end=" ")
        
        for next in range(len(graph[Start_V])):
            if (graph[go_to_v][next] == 1) and (next not in went):
                went.append(next)
                path.append(next)


N, M, V = map(int, input().split())

graph = [ [0] * (N+1) for _ in range(N+1) ]

for _ in range(M):
    p1, p2 = map(int, input().split())
    graph[p1][p2] = graph[p2][p1] = 1
    
DFS(graph, V)
print()
BFS(graph, V)