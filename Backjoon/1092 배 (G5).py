"""
BAEKJOON ALGORITHM
Date : 2022-03-19
Start Time : 14:54
End Time : 15:05
File Name : 1092 배 (G5)
URL : https://www.acmicpc.net/problem/1092
Category : Sorting
"""

import sys

N = int(sys.stdin.readline()) # 크레인의 갯수
Cranes = list(map(int, sys.stdin.readline().split())) # 크레인이 들 수 있는 무게

M = int(sys.stdin.readline()) # 박스의 갯수
Boxes = list(map(int, sys.stdin.readline().split())) # 박스의 무게

Cranes.sort(reverse=True) # 내림차순으로 정렬
Boxes.sort(reverse=True) # 내림차순으로 정렬

if Boxes[0] > Cranes[0]: # 옮길 수 없는 물건이 존재하는 경우
    print(-1)
else:
    result = 0 # 짐을 옮기는 데 걸리는 총 시간
    
    while Boxes: # 옮겨야 할 박스가 남아있는 경우
        for crane in Cranes:
            for box in Boxes:
                if crane >= box: # 물건을 옮길 수 있는 경우
                    Boxes.remove(box) # 물건을 옮긴다 (Boxes에서 box 삭제)
                    break # Boxes 순회 루프문 탈출
        result += 1
        
    print(result)