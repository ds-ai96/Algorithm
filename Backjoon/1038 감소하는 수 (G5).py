"""
BAEKJOON ALGORITHM
Date : 2022-03-15
Start Time : 20:40
End Time : 20:58
File Name : 1038 감소하는 수 (G5)
URL : https://www.acmicpc.net/problem/1038
Category : 	Bruteforcing
"""

import sys
from itertools import combinations

N = int(sys.stdin.readline()) 

decrease_number = []
for i in range(1, 11): # 0~9 중에서 선택하는 갯수 (1개 ~ 10개)
    for combination in combinations(range(0, 10), i): # 0~9의 수로 i자리 수 생성
        combination = list(combination)
        combination.sort(reverse=True) # 해당 조합을 감소하는 수로 만들기
        decrease_number.append(int("".join(map(str, combination))))

decrease_number.sort() # 감소하는 수를 오름차순으로 정렬

try: # N 번째 감소하는 수가 없는 경우를 위한 예외처리
    print(decrease_number[N])
except:
    print(-1)