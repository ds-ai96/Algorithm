"""
BAEKJOON ALGORITHM
Date : 2022-03-30
Start Time : 09:52
End Time : 10:27
File Name : 1987 알파벳 (G4)
URL : https://www.acmicpc.net/problem/1987
Category : DFS
"""

import sys

input = sys.stdin.readline

R, C = map(int, input().split())

board = [list(input()) for _ in range(R)]

move = [[1, 0], [-1, 0], [0, 1], [0, -1]] # 상, 하, 좌, 우 움직임을 결정하는 방향벡터

went = [0] * 26 # 지나왔던 알파벳을 체크 하는 리스트
went[ord(board[0][0])-65] = 1 # 시작점이 정해져 있으므로, 첫 칸을 미리 넣어두기

result = 1 # 움직일 수 있는 최대 거리, 첫 칸은 방문이므로 1

def DFS(x, y, cnt):
    
    global result
    result = max(result, cnt)
    
    for mx, my in move:
        dx = x + mx
        dy = y + my
        
        if (0 <= dx < R) and (0 <= dy < C) and (went[ord(board[dx][dy])-65] == 0):
            # 앞의 두 조건은 올바른 dx, dy 값인지 확인 ( board 내의 좌표인지 )
            # 마지막 조건은 다녀왔던 알파벳인지 확인
            went[ord(board[dx][dy])-65] = 1
            DFS(dx, dy, cnt+1) # dx, dy로 이동했을 때 실햄
            went[ord(board[dx][dy])-65] = 0 # 만약 dx, dy로 갔을 때 더 이상 이동할 수 없다면 다시 돌아와서 삭제

DFS(0, 0, result) # 시작점 [0][0]
print(result)