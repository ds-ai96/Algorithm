"""
BAEKJOON ALGORITHM
Date : 2022-03-03
Start Time : 15:11
End Time : 15:30
File Name : 3085 사탕 게임 (S3)
URL : https://www.acmicpc.net/problem/3085
Category : Bruteforcing
"""
import sys

input = sys.stdin.readline

N = int(input())
board = [list(input().rstrip()) for _ in range(N)]

def board_check(board):
    """
    보드에서 연속된 사탕의 갯수의 최댓값을 출력하는 함수
    """    
    n = len(board)
    result = 1
    
    for i in range(n):
        # 가로방향 체크하기
        cnt = 1
        for j in range(1, n):
            if board[i][j] == board[i][j-1]: # 왼쪽칸이랑 비교
                cnt += 1
            else: cnt = 1 # 왼쪽칸이랑 다르다면 cnt 초기화
            
            if cnt > result: result = cnt # cnt가 result보다 더 큰 경우 result 값 변경
            
        # 세로방향 체크하기
        cnt = 1
        for j in range(1, n):
            if board[j][i] == board[j-1][i]: # 위쪽칸이랑 비교
                cnt += 1
            else: cnt = 1# 위쪽칸이랑 다르다면 cnt 초기화
            
            if cnt > result: result = cnt # cnt가 result보다 더 큰 경우 result 값 변경
    return result

result = 0 # 결과값 저장하는 변수

# 모든 셀에 대해서 순회
for i in range(N):
    for j in range(N):
        # 세로방향 바꾸기
        if j+1 < N:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j] # i,j 위치의 사탕과 아래칸의 사탕 위치 바꾸기
            tmp = board_check(board) # 보드판 확인 / 결과값 임시저장하는 변수
            if tmp > result: result = tmp # 현재 결과값보다 더 큰 경우 결과값 변경
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j] # 사탕 바꾼것 원상복구
        
        # 가로방향 바꾸기
        if i+1 < N:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j] # i,j 위치의 사탕과 오른쪽칸의 사탕 위치 바꾸기
            tmp = board_check(board) # 보드판 확인 / 결과값 임시저장하는 변수
            if tmp > result: result = tmp # 현재 결과값보다 더 큰 경우 결과값 변경
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j] # 사탕 바꾼것 원상복구
            
print(result)