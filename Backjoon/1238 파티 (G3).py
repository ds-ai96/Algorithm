"""
BAEKJOON ALGORITHM
Date : 2022-04-13
Start Time : 11:38
End Time : 11:56
File Name : 1238 파티 (G3)
URL : https://www.acmicpc.net/problem/1238
Category : Dijkstra's Algorithm
"""
import heapq

N, M, X = map(int, input().split()) # N: 학생(마을)의 수, M: 도로(간선)의 갯수, X: 모여야 하는 마을
INF = 100 * 10000 # 최대 소요 시간 * 간선의 최대 갯수
graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))

def dijkstra(start):
    result = [INF] * (N+1)
    
    q = []
    heapq.heappush(q, (0, start))
    result[start] = 0
    
    while q:
        time, now = heapq.heappop(q)
        if result[now] >= time:
            for j in graph[now]:
                cost = time + j[1]
                if cost < result[j[0]]:
                    result[j[0]] = cost
                    heapq.heappush(q, (cost, j[0]))
    return result

ans = 0

for n in range(1, N+1):
    go = dijkstra(n)
    back = dijkstra(X)
    tmp = go[X] + back[n]
    ans = tmp if tmp > ans else ans
    
print(ans)