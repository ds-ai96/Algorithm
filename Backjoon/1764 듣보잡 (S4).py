"""
BAEKJOON ALGORITHM
Date : 2022-03-11
Start Time : 16:16
End Time : 
File Name : 1764 듣보잡 (S3)
URL : https://www.acmicpc.net/problem/1764
Category : Sorting
"""

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# 교집합 연산자 (&) 사용 및 중복을 피하기 위해 집합 자료형 사용
name_list1 = set() # 듣도 못한 사람
name_list2 = set() # 보도 못한 사람

for _ in range(N): # 듣도 못한 사람 이름 입력
    name_list1.add(input().rstrip())
    
for _ in range(M): # 보도 못한 사람 이름 입력
    name_list2.add(input().rstrip())

result = sorted(list(name_list1 & name_list2))

for content in result:
    print(content)