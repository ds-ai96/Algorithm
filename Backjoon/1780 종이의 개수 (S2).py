"""
BAEKJOON ALGORITHM
Date : 2022-03-14
Start Time : 11:41
End Time : 12:04
File Name : 1780 종이의 개수 (S2)
URL : https://www.acmicpc.net/problem/1780
Category : 	Recursion
"""
from re import X


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

result = [0] * 3 # 0, 1, 2(-1) 의 갯수를 저장하는 결과

def divide_paper(x, y, n):
    global result
    
    checker = paper[x][y] # 값 비교를 위해서 따로 변수에 저장
    
    for i in range(x, x + n): # 가로 비교
        for j in range(y, y + n): # 세로 비교
            if paper[i][j] != checker: # 같지 않으면 더 작은 조각으로 나눔
                for a in range(3):
                    for b in range(3):
                        divide_paper(x + a * n//3, y + b * n//3, n//3)
                return
    
    if checker == -1: result[-1] += 1
    elif checker == 1: result[1] += 1
    else: result[0] += 1
    
divide_paper(0, 0, N)

print(f"{result[-1]}\n{result[0]}\n{result[1]}")