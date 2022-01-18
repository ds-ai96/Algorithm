"""
BAEKJOON ALGORITHM
Date : 2022-01-03
Start Time 19:53 
End Time : 20:06
File Name : 10845 큐 (S4)
URL : https://www.acmicpc.net/problem/10845
Category : Data Structure - Queue
"""
from collections import deque
import sys

N = int(sys.stdin.readline())
queue = deque()

for _ in range(N):
    commend = sys.stdin.readline().split()

    if commend[0] == "push":
        queue.append(commend[1])
    
    elif commend[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()

    elif commend[0] == "size":
        print(len(queue))
    
    elif commend[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    
    elif commend[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    
    elif commend[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])