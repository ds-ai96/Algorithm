"""
BAEKJOON ALGORITHM
Date : 2022-04-06
Start Time : 14:31
End Time : 14:42
File Name : 2559 수열
URL : https://www.acmicpc.net/problem/2559
Category : Mathematics
"""

N, K = map(int, input().split())

C = list(map(int, input().split()))

range_sum = sum(C[:K])
result = [range_sum]

for idx in range(len(C)-K):
    range_sum = range_sum - C[idx] + C[idx+K]
    result.append(range_sum)
    
print(max(result))