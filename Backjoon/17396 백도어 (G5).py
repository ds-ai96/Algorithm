"""
BAEKJOON ALGORITHM
Date : 2022-04-261
Start Time : 14:32
End Time : 15:19
File Name : 17396 백도어 (G5)
URL : https://www.acmicpc.net/problem/17396
Category : Dijkstra's Algorithm
"""
import heapq
import sys

input = sys.stdin.readline

N, M = map(int, input().split()) # 노드 갯수, 간선 갯수
a = list(map(int, input().split())) # 상대편 시야 
a[-1] = 0 # 넥서스 위치

INF = 100000 * 300000 # 최대 시간 * 최대 간선 갯수
result = [INF] * N 
graph = [[] for _ in range(N)]

for _ in range(M):
    start, end, time = map(int, input().split())
    graph[start].append((end, time)) # 양방향성
    graph[end].append((start, time)) # 양방향성
        
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    result[start] = 0
    
    while q:
        time, now = heapq.heappop(q)
        if result[now] >= time:
            for x, y in graph[now]:
                cost = time + y
                if cost < result[x] and a[x] == 0:
                    result[x] = cost
                    heapq.heappush(q, (cost, x))
    return result

ans = dijkstra(0)[-1]
print(ans if ans != INF else -1)