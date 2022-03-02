"""
BAEKJOON ALGORITHM
Date : 2022-03-02
Start Time : 09:46
End Time : 10:59
File Name : 1406 에디터 (S3)
URL : https://www.acmicpc.net/problem/1406
Category : Data Structure - Stack
"""
import sys

word = list(sys.stdin.readline().rstrip())
stack = []

idx = len(word)
M = int(sys.stdin.readline())

for _ in range(M):
    oper = sys.stdin.readline().split()
    
    if oper[0] == "L" and word:
        stack.append(word.pop())
    elif oper[0] == "D" and stack:
        word.append(stack.pop())
    elif oper[0] == "B" and word:
        word.pop()
    elif oper[0] == "P":
        word.append(oper[1])
        
print("".join(word + list(reversed(stack))))