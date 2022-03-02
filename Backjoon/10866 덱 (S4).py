"""
BAEKJOON ALGORITHM
Date : 2022-03-02
Start Time : 12:34
End Time : 13:15
File Name : 10866 덱 (S4)
URL : https://www.acmicpc.net/problem/10866
Category : Data Structure - Deque
"""
import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()

def empty():
    if len(queue) == 0:
        return 1
    else:
        return 0

for _ in range(N):
    oper = list(sys.stdin.readline().split())
    
    if oper[0] == "push_front":
        queue.appendleft(oper[1])
        
    elif oper[0] == "push_back":
        queue.append(oper[1])
        
    elif oper[0] == "pop_front":
        if len(queue) == 0: print(-1)
        else:
            tmp = queue.popleft()
            print(tmp)
        
    elif oper[0] == "pop_back":
        if len(queue) == 0: print(-1)
        else:
            tmp = queue.pop()
            print(tmp)
        
    elif oper[0] == "size":
        print(len(queue))
        
    elif oper[0] == "empty": 
        if len(queue) == 0: print(1)
        else: print(0)
    
    elif oper[0] == "front":
        if len(queue) == 0: print(-1)
        else: print(queue[0])
            
    elif oper[0] == "back":
        if len(queue) == 0: print(-1)
        else: print(queue[len(queue)-1])