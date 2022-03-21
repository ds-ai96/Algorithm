"""
BAEKJOON ALGORITHM
Date : 2022-03-21
Start Time : 20:01
End Time : 20:04
File Name : 11005 진법 변환 2 (B1)
URL : https://www.acmicpc.net/problem/11005
Category : Mathematics
"""

import sys

words = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" # 0부터 36까지 숫자를 미리 정의

N, B = map(int, sys.stdin.readline().split())

result = ""

while N != 0:
    result += str(words[N % B]) # 나머지가 해당 자리의 숫자에 해당
    N = N // B
    
print(result[::-1])
    