"""
BAEKJOON ALGORITHM
Date : 2022-01-04
Start Time : 10:42 
End Time : 11:35
File Name : 1914 하노이 탑 (S2)
URL : https://www.acmicpc.net/problem/1914
Category : Recursion
"""

def hanoi(start, tmp, end, N):
    
    if N == 1:
        print(f"{start} {end}")
        return
    
    else:
        hanoi(start, end, tmp, N-1)
        print(f"{start} {end}")
        hanoi(tmp, start, end, N-1)


N = int(input())
start, tmp, end = 1, 2, 3

if N <= 20:
    print((1<<N) - 1)
    hanoi(start, tmp, end, N)
    
else: print((1<<N) - 1)