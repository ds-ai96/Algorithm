"""
BAEKJOON ALGORITHM
Date : 2022-02-18
Start Time : 16:05
End Time : 16:25
File Name : 1874 스택 수열 (S3)
URL : https://www.acmicpc.net/problem/1874
Category : Data Structure - Stack
"""
import sys

input = sys.stdin.readline

n = int(input())
count = 0
stack = [] # 숫자를 담는 리스트
result = [] # +, - 를 담는 리스트
NO = False


for i in range(n): # n번 반복
    number = int(input())
    
    while count < number:
        count += 1
        stack.append(count)
        result.append("+")
        
    if stack[-1] == number:
        stack.pop()
        result.append("-")
    
    else:
        NO = True
        break
        
if NO == True:
    print("NO")
else:
    print("\n".join(result))
    