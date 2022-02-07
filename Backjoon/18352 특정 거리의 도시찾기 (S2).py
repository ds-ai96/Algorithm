"""
BAEKJOON ALGORITHM
Date : 2022-02-07
Start Time : 14:20
End Time : 14:54
File Name : 18352 특정 거리의 도시 찾기 (S2)
URL : https://www.acmicpc.net/problem/18352
Category : Dijkstra's Algorithm
"""
import heapq
import sys

N, M, K, X = map(int, sys.stdin.readline().split())
INF = 300000 # 300000은 간선 길이의 최댓값
graph = [[] for _ in range(N+1)]
result = [INF] * (N+1)

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append((end, 1))
    
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

dijkstra(X) # X (시작점) 에서 시작하는 최단경로
ans = []
for i in range(1, N+1):
    if result[i] == K:
        ans.append(i)
    
if len(ans) == 0:
    print(-1)
    
else:
    for i in ans:
        print(i, end="\n")