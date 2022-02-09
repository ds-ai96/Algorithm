"""
BAEKJOON ALGORITHM
Date : 2022-02-09
Start Time : 16:17
End Time : 16:29
File Name : 1916 최소비용 구하기 (G5)
URL : https://www.acmicpc.net/problem/1916
Category : Dijkstra's Algorithm
"""

import heapq
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

INF = 100000 * 1000 # 버스비용의 최댓값 * 도시의 최대 갯수
graph = [[] for _ in range(N+1)]
result = [INF] * (N+1)

# graph 초기화
for _ in range(M):
    start, end, weight = map(int, sys.stdin.readline().split())
    graph[start].append((end, weight))
    
Start, End = map(int, sys.stdin.readline().split())

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
                    
dijkstra(Start)

print(result[End])
