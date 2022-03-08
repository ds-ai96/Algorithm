"""
BAEKJOON ALGORITHM
Date : 2022-03-08
Start Time : 11:04
End Time : 11:23
File Name : 13414 수강신청 (S3)
URL : https://www.acmicpc.net/problem/13414
Category : Implementation
"""
import sys

K, L = map(int, sys.stdin.readline().split())
sugang = dict()

for idx in range(L):
    tmp = sys.stdin.readline().rstrip()
    sugang[tmp] = idx

sugang = sorted(sugang.items(), key=(lambda x: x[1]))

cnt = 0
for student in sugang:
    if cnt == K:
        break
    print(student[0])
    cnt += 1