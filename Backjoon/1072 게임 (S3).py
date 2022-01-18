"""
BAEKJOON ALGORITHM
Date : 2022-01-17
Start Time : 09:37
End Time : 10:14
File Name : 1072 게임 (S3)
URL : https://www.acmicpc.net/problem/1072
Category : Binary Search
"""

X, Y = map(int, input().split()) # X 진행한 게임의 수, Y 승리한 게임의 수

win_rate = Y * 100 // X # 초기 조건에 대한 승률
result = float("inf") # 최댓값
start, end = 1, X

while start <= end:
    mid = (start + end) // 2 # 더 진행해야 하는 게임 수
    
    current_win_rate = (Y + mid) * 100 // (X + mid) # 게임을 mid 만큼 진행했을 때 승률
    
    if current_win_rate > win_rate:
        result = min(mid, result)
        end = mid - 1
    else:
        start = mid + 1
        
if result == float("inf"):
    print(-1)
else:
    print(result)
