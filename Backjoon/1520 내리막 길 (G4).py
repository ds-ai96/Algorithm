"""
BAEKJOON ALGORITHM
Date : 2022-03-30
Start Time : 10:25
End Time : 10:42
File Name : 1520 내리막 길
URL : https://www.acmicpc.net/problem/1520
Category : DFS & DP
"""
import sys
sys.setrecursionlimit(10 ** 6)

M, N = map(int, input().split()) # 세로, 가로의 크기

map = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
move = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def DFS(x, y):
    if x == M-1 and y == N-1: # 도착지점
        return 1
    if dp[x][y] != -1: # 이전에 방문했던(계산이 된) 지점
        return dp[x][y]
    
    dp[x][y] = 0 # 방문 확인
    
    for mx, my in move: # 이동하는 방법
        dx = x + mx
        dy = y + my
            
        if 0 <= dx < M and 0 <= dy < N and map[dx][dy] < map[x][y]:
            dp[x][y] += DFS(dx, dy)
    return dp[x][y]

print(DFS(0, 0))