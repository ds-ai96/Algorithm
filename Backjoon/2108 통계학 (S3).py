"""
BAEKJOON ALGORITHM
Date : 2022-03-07
Start Time : 10:54
End Time : 11:30
File Name : 2108 통계학 (S3)
URL : https://www.acmicpc.net/problem/2108
Category : Mathematics
"""
import sys, collections

N = int(sys.stdin.readline())
numbers = []

for _ in range(N):
    numbers.append(int(sys.stdin.readline()))
    
numbers.sort()

print(round(sum(numbers) / len(numbers))) # 산술평균
print(numbers[N//2]) # 중간값

counts = collections.Counter(numbers).most_common()
if len(counts) > 1: # 최빈값
    if counts[0][1] == counts[1][1]:
        print(counts[1][0])
    else: print(counts[0][0])
else:
    print(counts[0][0])

print(numbers[-1] - numbers[0]) # 범위