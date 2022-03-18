"""
BAEKJOON ALGORITHM
Date : 2022-03-17
Start Time : 10:44
End Time : 11:01
File Name : 19942 다이어트 (G5)
URL : https://www.acmicpc.net/problem/19942
Category : 	Bruteforcing
"""

import sys
from itertools import combinations

N = int(sys.stdin.readline())
mp, mf, ms, mv = map(int, sys.stdin.readline().split())

food_table = [[]] # 음식의 인덱스는 1번부터 시작

for _ in range(N):
    food_table.append(list(map(int, sys.stdin.readline().split())))

result = None
compare_c = 500 * 15 + 1 # 입력받을 수 있는 최대의 가격 + 1

for num in range(1, N+1): # 1개부터 N개까지 조합을 구성할 음식의 갯수
    for comb in combinations(range(1, N+1), num): # 결과를 인덱스로 출력해야하므로 인덱스로 조합을 구성
        p = f = s = v = c = 0 # 결과 단백질, 지방, 탄수화물, 비타민, 가격
        for t in comb:
            p += food_table[t][0]
            f += food_table[t][1]
            s += food_table[t][2]
            v += food_table[t][3]
            c += food_table[t][4]
            
        if p >= mp and f >= mf and s >= ms and v >= mv:
            if compare_c > c:
                compare_c = c
                result = comb
            
            elif compare_c == c:
                result = sorted([result, comb])[0] # 사전순으로 정렬해서 첫번째 것만 저장

if compare_c == 500 * 15 + 1: # 값 변화가 없이 초기와 동일하면 만족하는 답 없음
    print(-1)

else: # 만족하는 답이 있는 경우
    print(compare_c) # 최소가격 출력하기
    print(*result) # 만족하는 음식의 인덱스를 출력
