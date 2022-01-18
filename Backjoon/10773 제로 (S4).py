"""
BAEKJOON ALGORITHM
Date : 2022-01-03
Start Time 19:46
End Time 19:52 
File Name : 10773 제로 (S4)
URL : https://www.acmicpc.net/problem/10773
Category : Data Structure - Stack
"""

K = int(input())
Stack = []
for _ in range(K):
    tmp = int(input())
    
    if tmp == 0:
        Stack.pop()
    
    else:
        Stack.append(tmp)
        
print(sum(Stack))    