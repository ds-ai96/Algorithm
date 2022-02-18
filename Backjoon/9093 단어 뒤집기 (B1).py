"""
BAEKJOON ALGORITHM
Date : 2022-02-18
Start Time : 15:39
End Time : 15:44
File Name : 9093 단어 뒤집기 (B1)
URL : https://www.acmicpc.net/problem/9093
Category : Data Structure - String
"""
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    words = list(input().split())
    
    for word in words:
        print(word[::-1], end = " ")