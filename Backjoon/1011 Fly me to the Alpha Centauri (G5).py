"""
BAEKJOON ALGORITHM
Date : 2022-02-15
Start Time : 13:17
End Time : 13:40
File Name : 1011 Fly me to the Alpha Centauri (G5)
Category : Mathematics
"""
import sys

T = int(sys.stdin.readline()) # Test Case

for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    distance = y - x
    
    move_count = 0 # 우주선이 움직인 횟수
    possible_move = 1   # 우주선이 움직일 수 있는 거리
    total_move = 0  # 우주선이 총 이동한 거리의 함
    
    while total_move < distance:
        move_count += 1
        total_move += possible_move
        
        if move_count % 2 == 0:
            possible_move += 1
    print(move_count)