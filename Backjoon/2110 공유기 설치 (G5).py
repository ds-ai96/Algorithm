"""
BAEKJOON ALGORITHM
Date : 2022-01-21
Start Time : 10:24
End Time : 10:45
File Name : 2110 공유기 설치 (G5)
URL : https://www.acmicpc.net/problem/2110
Category : Binary Search
"""

N, C = map(int, input().split()) # 집의 갯수 N개, 공유기의 갯수 C개

home_xi = [] # 집의 좌표들을 저장할 리스트 생성
for _ in range(N):
    home_xi.append(int(input()))
    
home_xi.sort()

start = 1; end = home_xi[-1] - home_xi[0] # start: 최소 거리, end: 최대 거리
result = 0

while (start <= end):
    mid = (start+end) // 2 # 가장 인접한 두 공유기 사이의 최대 거리
    network = home_xi[0]
    count = 1
    
    for i in range(1, len(home_xi)):
        if home_xi[i] >= network + mid:
            count += 1
            network = home_xi[i]
            
    if count >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
    
print(result)