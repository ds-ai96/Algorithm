"""
BAEKJOON ALGORITHM
Date : 2022-03-31
Start Time : 15:50
End Time : 16:12
File Name : 2655 가장높은탑쌓기
URL : https://www.acmicpc.net/problem/2655
Category : Dynamic Programming
"""

N = int(input()) # 블럭의 갯수

blocks = [(0, 0, 0, 0)] # 0번 index 미리 추가해서 생성
for idx in range(N):
    area, height, weight = map(int, input().split())
    blocks.append((idx+1, area, height, weight))

blocks.sort(key=lambda x: x[3]) # 무게 순으로 오름차순 정렬 (무조건 뒤의 블럭이 아래에 쌓일 가능성이 있다.)

dp = [0] * (N+1)

for i in range(1, N+1):
    for j in range(0, i):
        if blocks[j][1] < blocks[i][1]: # 무게가 무거운 벽돌이 밑면의 면적도 큰 경우
            dp[i] = max(dp[i], dp[j] + blocks[i][2])
       
HEIGHT = max(dp)
idx = dp.index(HEIGHT)
result = []

while idx != 0:
    if HEIGHT == dp[idx]:
        result.append(blocks[idx][0])
        HEIGHT -= blocks[idx][2]
    idx -= 1
    
print(len(result))
print(*result[::-1], sep="\n")