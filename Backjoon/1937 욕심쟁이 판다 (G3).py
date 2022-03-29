"""
BAEKJOON ALGORITHM
Date : 2022-03-29
Start Time : 09:47
End Time : 10:37
File Name : 1937 욕심쟁이 판다
URL : https://www.acmicpc.net/problem/1937
Category : Dynamic Programming
"""
from sys import setrecursionlimit
setrecursionlimit(10**9)

n = int(input())

bamboos = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]  # dp 테이블 초기화

move = [[1, 0], [-1, 0], [0, 1], [0,-1]] # 상하좌우 움직일 수 있는 방향벡터

def DFS(x, y):
    if dp[x][y] == 0: # 처음 방문한 경우
        dp[x][y] = 1 # 방문 확인
        
        for mx, my in move: # 판다가 움직이는 경우를 고려
            dx = x + mx # 방향 벡터만큼 움직인 후의 x 위치
            dy = y + my # 방향 벡터만큼 움직인 후의 y 위치
            
            if 0 <= dx < n and 0 <= dy < n and bamboos[x][y] < bamboos[dx][dy]:
                # 앞의 2 조건은 올바른 dx, dy 값인지 확인
                # 마지막 조건은 판다가 이동할 수 있는지 확인
                dp[x][y] = max(dp[x][y], DFS(dx, dy)+1) # dp는 움직인 횟수이므로, 처음 풀어준 칸을 더해줘야 한다.
                
    return dp[x][y]


result = 0

# 시작 지점이 정해지지 않았으므로, 모든 지점에 대해서 검사한다.
for i in range(n):
    for j in range(n):
        result = max(result, DFS(i, j))

print(result)  