"""
BAEKJOON ALGORITHM
Date : 2022-01-05
Start Time : 19:07
End Time : 19:20
File Name : 1850 최대공약수 (S2)
URL : https://www.acmicpc.net/problem/1850
Category : Recursion
"""

def GCD(A, B):
    if B == 0:
        return A
    else:
        return GCD(B, A%B)
    

A, B = map(int, input().split())

result = GCD(A, B)
print("1" * result)