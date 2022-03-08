"""
BAEKJOON ALGORITHM
Date : 2022-03-08
Start Time : 11:37
End Time : 11:53
File Name : 1138 한 줄로 서기 (S2)
URL : https://www.acmicpc.net/problem/1138
Category : Implementation
"""
import sys

N = int(input())
idx = list(map(int, sys.stdin.readline().split()))

result = [0] * N

for high in range(1, N+1): # 키가 1인사람부터 N인 사람까지 반복
    left_tall = idx[high-1]
    cnt = 0
    
    for place in range(N): # 자리에 사람을 배정하기 위한 반복문
        if cnt == left_tall and result[place] == 0: # 왼쪽 큰 사람 수가 cnt 와 같고, place 번째 자리가 비어있을 경우
            result[place] = high # place에 키가 high인 사람을 배치
            break
        elif result[place] == 0: # place가 비어있다면, cnt만 1 증가
            cnt += 1

print(*result)