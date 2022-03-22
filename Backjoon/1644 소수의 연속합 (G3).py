"""
BAEKJOON ALGORITHM
Date : 2022-03-22
Start Time : 13:53
End Time : 14:04
File Name : 1644 소수의 연속합 (G3)
URL : https://www.acmicpc.net/problem/1644
Category : Mathematics
"""

MAX = 4000000 # N의 최댓값
prime_number_idx = [True for _ in range(MAX + 1)] # 소수를 나타낼 행렬

for number in range(2, int(MAX ** 0.5)):
    if prime_number_idx:
        for idx in range(number+number, MAX+1, number):
            prime_number_idx[idx] = False
            
prime_number = [idx for idx, number in enumerate(prime_number_idx) if number == True and idx >= 2]

N = int(input())

# 투포인트
result = 0
start = 0
end = 0

while (end >= start) and (end <= len(prime_number)):
    if sum(prime_number[start:end+1]) == N: # 구간 합과 소수가 같은 경우
        result += 1
        start += 1
    
    elif sum(prime_number[start:end+1]) > N: # 구간 합이 소수보다 큰 경우
        start += 1
    else: # 구간 합이 소수보다 작은 경우
        end += 1
        
print(result)