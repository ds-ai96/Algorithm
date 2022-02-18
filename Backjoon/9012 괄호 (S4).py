"""
BAEKJOON ALGORITHM
Date : 2022-02-18
Start Time : 15:51
End Time : 15:59
File Name : 9012 괄호 (S4)
URL : https://www.acmicpc.net/problem/9012
Category : Data Structure - Stack
"""
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    
    input_list = list(input())
    stack = []
    
    for Par in input_list[:-1]:
        if len(stack) == 0:
            stack.append(Par)
        
        elif Par==")" and stack[-1] == "(":
            stack.pop()
            
        else:
            stack.append(Par)
            
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")