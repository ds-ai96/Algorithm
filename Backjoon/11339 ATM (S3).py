"""
BAEKJOON ALGORITHM
Date : 2021-12-29
Start Time : 17:12
End Time : 17:23
File Name : 11399 ATM (S3)
Category : Greedy
"""
    
N = int(input())
P = list(map(int, input().split()))

P.sort()

result = 0

for i in range(1, len(P)+1):
    result += sum(P[:i])

print(result)