"""
BAEKJOON ALGORITHM
Date : 2022-04-08
Start Time : 20:41
End Time : 21:14
File Name : 16400 소수 화폐
URL : https://www.acmicpc.net/problem/16400
Category : Mathematics
"""

# PyPy3

N = int(input())

prime_number_idx = [True] * (N+1)

for number in range(2, N+1):
    if prime_number_idx[number]:
        for idx in range(number << 1, N+1, number):
            prime_number_idx[idx] = False

prime_number = []

for num in range(2, N+1):
    if prime_number_idx[num]:
        prime_number.append(num)

dp = [0] * 40001
dp[0] = 1

for prime in prime_number:
    for N_idx in range(prime, N+1):
        dp[N_idx] = (dp[N_idx] + dp[N_idx - prime]) % 123456789

print(dp[N])