"""
BAEKJOON ALGORITHM
Date : 2022-03-13
Start Time : 15:33
End Time : 16:30
File Name : 11000 강의실 배정 (G5)
URL : https://www.acmicpc.net/problem/11000
Category : Greedy
"""
import heapq, sys

N = int(input())
classroom = []

lectures = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    
lectures.sort(key = lambda x:x[0])

heapq.heappush(classroom, lectures[0][1]) # 첫번째 강의가 끝나는 시간을 추가

for idx in range(1, N): # 2번째 강의부터 마지막 강의까지 반복
    if classroom[0] > lectures[idx][0]: # 이전 강의의 끝나는 시간과 다음 강의의 시작 시간을 비교
        # 만약 이전 강의가 더 늦게 끝나면 (다음 회의 시작이 더 빠르면)
        heapq.heappush(classroom, lectures[idx][1]) # 새로운 강의실 생성
    else: # 현재 강의실에서 연달아 강의 가능
        heapq.heappop(classroom) # 다음 강의 종료시간으로 변경 위해서 pop
        heapq.heappush(classroom, lectures[idx][1]) # 다음 강의의 종료 시간을 push
print(len(classroom))