"""
BAEKJOON ALGORITHM
Date : 2022-02-16
Start Time : 13:19
End Time : 13:39
File Name : 17427 약수의 합 2 (S2)
URL : https://www.acmicpc.net/problem/17427
Category : Mathematics
"""

import sys

N = int(sys.stdin.readline())
result = 0 # 최종 결과값을 저장하는 변수

for iter in range(1, N+1): # 1부터 N까지 수 반복
    result += (N//iter) * iter # iter을 약수로 가지는 수

print(result)