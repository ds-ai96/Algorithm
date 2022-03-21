"""
BAEKJOON ALGORITHM
Date : 2022-03-21
Start Time : 20:08
End Time : 20:32
File Name : 2749 피보나치 수 3 (G2)
URL : https://www.acmicpc.net/problem/2749
Category : Mathematics
"""

N = int(input())

mod = 1000000 # 1000000으로 나눈 나머지를 구하기 위해 나누는 수인 mod를 정의
fibo = [0, 1] # 피보나치 수열이 저장 되는 리스트
period = 1500000 # 피보나치 수열이 반복되는 주기 - 주기를 구하는 예제코드 참고

for idx in range(2, period):
    fibo.append((fibo[idx-1] + fibo[idx-2]) % mod)

print(fibo[N % period])


# 주기 period를 구하기 위한 코드
# N = [0, 1]
# cycle = []
# for idx in range(2, 10000000):
#     N.append((N[idx-1] + N [idx-2]) % 1000000)

#     if N[-1] == 346269: # 처음으로 1000000을 넘어서는 숫자 (31번 인덱스)
#         cycle.append(idx)

# period = []
# for idx in range(1, len(cycle)):
#     period.append(cycle[idx-1] - cycle[idx])
    
# print(period) # 3번씩 반복되는 것을 확인
# print(sum(period[:3])) # 반복주기를 확인하기 위해서 반복되는 3번을 다 합함 -> 1500000