"""
BAEKJOON ALGORITHM
Date : 2022-01-20
Start Time : 11:54
End Time : 12:32
File Name : 2343 기타 레슨 (S1)
URL : https://www.acmicpc.net/problem/2343
Category : Binary Search
"""

def study_time_check(study_time, mid):
    count = 0; study_in_disk = 0 # 필요한 블루레이 디스크의 갯수, 하나의 블루레이 디스크에 들어가는 강의 시간의 합
    for i in range(len(study_time)):
        if study_in_disk + study_time[i] > mid:
            count += 1
            study_in_disk = 0
        study_in_disk += study_time[i]
    if study_in_disk:
        count += 1
    return count

N, M = map(int, input().split()) # 강의의 수 N개, 블루레이의 갯수 M개
study_time = list(map(int, input().split())) # 각 강의의 시간 리스트

start = max(study_time); end = sum(study_time)

while (start <= end):
    mid = (start + end) // 2
    count = study_time_check(study_time, mid)
            
    if count <= M:
        end = mid - 1
    else:
        start = mid + 1

print(start)
