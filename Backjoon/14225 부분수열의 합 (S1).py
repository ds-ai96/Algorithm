"""
BAEKJOON ALGORITHM
Date : 2022-04-07
Start Time : 13:28
End Time : 13:35
File Name : 14225 부분수열의 합
URL : https://www.acmicpc.net/problem/14225
Category : Bruteforcing
"""
from itertools import combinations

N = int(input())
S = list(map(int, input().split()))

result = [True] * (sum(S)+2) # 0부터 S까지
for length in range(1, len(S)+1):
    subsets = combinations(S, length)
    for subset in subsets:
        tmp = sum(subset)
        result[tmp] = False

for idx in range(1, len(result)):
    if result[idx] == True:
        print(idx)
        break
    