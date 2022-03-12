"""
BAEKJOON ALGORITHM
Date : 2022-03-12
Start Time : 20:47
End Time : 21:05
File Name : 2217 로프 (S4)
URL : https://www.acmicpc.net/problem/2217
Category : Greedy
"""

N = int(input())

ropes = [] # 로프의 길이를 저장하기 위함

for _ in range(N):
    ropes.append(int(input()))

ropes.sort(reverse=True) # 내림차순으로 정렬

result = [] # 결과값들
for num in range(N): # rope를 여러개를 쓰는 경우
    # 최대 무게 견디는 로프 기준으로 1개씩 로프를 늘려가면서 계산
    # ropes[num]은 로프들 중에서 가장 적은 무게를 견디는 로프 * 로프들의 갯수
    result.append(ropes[num] * (num+1))
    
print(max(result))