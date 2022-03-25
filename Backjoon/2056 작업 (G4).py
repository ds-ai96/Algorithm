"""
BAEKJOON ALGORITHM
Date : 2022-03-25
Start Time : 13:56
End Time : 14:27
File Name : 2056 작업 (G4)
URL : https://www.acmicpc.net/problem/2056
Category : Dynamic Programming
"""

N = int(input())

works = [0] * (N+1)

for idx in range(N):
    works[idx+1] = list(map(int, input().split()))

dp = [0] * (N+1) # [종료시간] * (작업 수 + 1)

for work_idx in range(1, len(works)): # work_idx은 idx 번째 작업을 의미
    if works[work_idx][1] == 0: # 사전에 수행해야 하는 작업이 없는 경우
        dp[work_idx] = works[work_idx][0] # 종료시간은 작업 총 소요시간
        
    else: # 사전에 수행하야 하는 작업이 있는 경우
        for work_iter in works[work_idx][2:]: # 수행해야 하는 작업 갯수 많큼 반복
            dp[work_idx] = max(dp[work_idx], dp[work_iter] + works[work_idx][0]) # 사전 작업의 종료시간 + 해야하는 일의 소요시간

print(max(dp)) # 가장 마지막 작업의 끝나는 시간 출력
        