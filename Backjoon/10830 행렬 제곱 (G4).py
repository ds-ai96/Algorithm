"""
BAEKJOON ALGORITHM
Date : 2022-03-22
Start Time : 13:14
End Time : 13:52
File Name : 10830 행렬 제곱 (G4)
URL : https://www.acmicpc.net/problem/10830
Category : Mathematics
"""
import sys

def matrix_power(N, A, B):
    result = [[0] * N for _ in range(N)] # 결과를 저장할 행렬 생성
    
    # 행렬의 곱 계산
    for row in range(N):
        for col in range(N):
            for idx in range(N):
                result[row][col] += A[row][idx] * B[idx][col]
            
            result[row][col] %= 1000 # 1000으로 나눈 나머지로 변환            
    return result

def matrix_devide(N, B, A):
    if B == 1:
        for row in range(N):
            for col in range(N):
                A[row][col] %= 1000
        return A
    else:
        half = matrix_devide(N, B // 2, A) # 절반으로 분할한 문제
        if B % 2 == 0:
            return matrix_power(N, half, half) # A^B = A^(B//2) * A^(B//2)
        else:
            return matrix_power(N, matrix_power(N, half, half), A) # A^B = A^(B//2) * A^(B//2) * A

N, B = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = matrix_devide(N, B, A)

for row in result:
    print(*row)