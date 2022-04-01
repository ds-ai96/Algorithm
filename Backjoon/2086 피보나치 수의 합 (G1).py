"""
BAEKJOON ALGORITHM
Date : 2022-04-01
Start Time : 11:24
End Time : 13:09
File Name : 2086 피보나치 수의 합
URL : https://www.acmicpc.net/problem/2086
Category : Mathematics
"""

# 1~N까지의 합은 N+2 번째 피보나치 - 1
MOD = 1000000000

MATRIX = [[1, 1], [1, 0]] # 피보나치 구하는 행렬
DIAG = [[1, 0], [0, 1]] # 대각 행렬
FIBO_MATRIX = [1, 1] # 2번째 피보나치 수, 1번째 피보나치 수

def matrix_mul(A, B): # 2x2 고정이므로 우선 단순하게 정의
    return ([[A[0][0]*B[0][0]%MOD + A[0][1]*B[1][0]%MOD, A[0][0]*B[0][1]%MOD + A[0][1]*B[1][1]%MOD],
             [A[1][0]*B[0][0]%MOD + A[1][1]*B[1][0]%MOD, A[1][0]*B[0][1]%MOD + A[1][1]*B[1][1]%MOD]]
)

def matrix_power(A, n):
    diag = DIAG
    while True:
        if n == 1: 
            return A
        if n % 2 == 0:
            tmp = matrix_power(A, n//2)
            return matrix_mul(tmp, tmp)
        else:
            tmp = matrix_power(A, n-1)
            return matrix_mul(tmp, A)

def FIBO_N(n):
    FIBO = matrix_power(MATRIX, n)
    return FIBO[0][1] % MOD# n번째 피보나치 숫자

a, b = map(int, input().split())

# (b번째 피보나치 수 까지의 합) - (a-1 번째 피보나치 수 까지의 합)
# = (b+2 번째 피보나치 수 - 1) - (a+1 번째 피보나치 수 - 1)
# = (b+2 번째 피보나치 수 - a+1 번째 피보나치 수)

result = FIBO_N(b+2) - FIBO_N(a+1)
if result < 0: # 나머지로 미리 나누었기 때문에, 음수가 나올 수 있음
    result += MOD

print(result)