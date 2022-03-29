"""
BAEKJOON ALGORITHM
Date : 2022-03-29
Start Time : 10:39
End Time : 11:28
File Name : 2533 사회망 서비스 (SNS)
URL : https://www.acmicpc.net/problem/2533
Category : Dynamic Programming
"""
import sys
sys.setrecursionlimit(10 ** 9)

N = int(sys.stdin.readline())
friend_tree = [[] for _ in range(N+1)]

for _ in range(N-1): # 사이클이 없는 트리이기 때문에 간선의 갯수는 N-1개
    v1, v2 = map(int, sys.stdin.readline().split())
    friend_tree[v1].append(v2)
    friend_tree[v2].append(v1)

dp = [[0, 0] for _ in range(N+1)]
# dp[current][0] => current가 얼리어답터일 때
# dp[current][1] => current가 얼리어답터가 아닐 때

visited = [0 for _ in range(N+1)]

def DFS(current):
    visited[current] = 1 # 방문하면 1로 변경
    dp[current][0] = 1 # 자기자신이 얼리어답터 이므로, 얼리어답터의 최소 수는 1
    
    for vertex in friend_tree[current]: # 트리 순회
        if visited[vertex] == 0: # 정점에 방문 하지 않았으면 방문 해야 함
            DFS(vertex)
            dp[current][0] += min(dp[vertex][0], dp[vertex][1]) # vertex가 얼리어답터인 경우
            dp[current][1] += dp[vertex][0] # vertex가 얼리어답터가 아닌 경우
            
DFS(1)
print(min(dp[1][0], dp[1][1]))