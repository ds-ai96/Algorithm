"""
BAEKJOON ALGORITHM
Date : 2022-03-07
Start Time : 11:54
End Time : 12:03
File Name : 1629 곱셈 (S1)
URL : https://www.acmicpc.net/problem/1629
Category : Mathematics
"""
import sys

def power(A, B): # 거듭제곱의 횟수를 반으로 줄여서 풀기
    if B == 1: # 1의 거듭제곱인 경우
        return A % C
    
    else: # 거듭제곱의 차수가 2 이상인 경우
        tmp = power(A, B // 2) # 미리 B를 2로 나눈 경우를 계산한다.
        if B % 2 == 0: # B가 짝수인 경우
            return tmp * tmp % C
        else: # B가 홀수인 경우
            return tmp * tmp * A % C
    
A, B, C = map(int, sys.stdin.readline().split())

result = power(A, B)
print(result)