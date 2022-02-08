"""
BAEKJOON ALGORITHM
Date : 2022-02-08
Start Time : 19:15
End Time : 19:30
File Name : 1753 최단경로 (G5)
URL : https://www.acmicpc.net/problem/1753
Category : Dijkstra's Algorithm
"""

import heapq
import sys

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
INF = 3000000 # 최대 간선 갯수 (300,000) * 최대 가중치 (10)
graph = [[] for _ in range(V+1)]
result = [INF] * (V+1)

for _ in range(E):
    start, end, weight = map(int, sys.stdin.readline().split())
    graph[start].append((end, weight))
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    result[start] = 0
    
    while q:
        distance, now = heapq.heappop(q)
        if result[now] >= distance:
            for j in graph[now]:
                cost = distance + j[1]
                if cost < result[j[0]]:
                    result[j[0]] = cost
                    heapq.heappush(q, (cost, j[0]))

dijkstra(K)
for idx in range(len(result)):
    if result[idx] == 3000000:
        result[idx] = "INF"
        
for e in result[1:]:
    print(e)