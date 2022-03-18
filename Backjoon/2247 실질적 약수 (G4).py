"""
BAEKJOON ALGORITHM
Date : 2022-03-18
Start Time : 11:00
End Time : 11:33
File Name : 2247 실질적 약수 (G4)
URL : https://www.acmicpc.net/problem/2247
Category : Mathematics
"""
import sys

N = int(sys.stdin.readline())

CSOD = 0
for num in range(2, N // 2 +1):
    CSOD += (N // num - 1) * num
    
print(CSOD % 1000000)