"""
BAEKJOON ALGORITHM
Date : 2022-03-24
Start Time : 14:23
End Time : 14:47
File Name : 5052 전화번호 목록 (G4)
URL : https://www.acmicpc.net/problem/5052
Category : Sorting
"""
import sys

T = int(sys.stdin.readline()) # Test Case

for _ in range(T): # Test Case 만큼 반복
    N = int(sys.stdin.readline())
    tels = [sys.stdin.readline().rstrip() for _ in range(N)]
    tels.sort()
    
    result = True
    for idx in range(len(tels) - 1):
        length = len(tels[idx])
        if tels[idx] == tels[idx + 1][:length]:
            result = False
        
    if result:
        print("YES")
    else:
        print("NO")