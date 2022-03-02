"""
BAEKJOON ALGORITHM
Date : 2022-03-02
Start Time : 09:37
End Time : 09:45
File Name : 1158 요세푸스 문제 (S5)
URL : https://www.acmicpc.net/problem/1158
Category : Data Structure - Queue
"""

from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())

init_list = [x for x in range(1, N+1)]

result = []
idx = 0

for num in range(N):
    idx += K-1 # K 번째 사람이 제거되도록 인덱스 설정
    if idx >= len(init_list): # 한 바퀴를 도는 경우
        idx = idx % len(init_list)
        
    result.append(str(init_list.pop(idx))) # K 번째 사람을 제거하고, 결과 리스트에 추가
    
print("<", ", ".join(result),">", sep="")
    