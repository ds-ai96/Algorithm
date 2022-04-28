"""
BAEKJOON ALGORITHM
Date : 2022-04-28
Start Time : 21:35
End Time : 21:49
File Name : 2981 검문 (G5)
URL : https://www.acmicpc.net/problem/2981
Category : Mathematics
"""
import sys, math

input = sys.stdin.readline

T = int(input())
N = []

for _ in range(T):
    N.append(int(input()))
    

N.sort() # 오름차순으로 정렬

numbers = [] # N[i] - N[i-1] 저장

for idx in range(T-1):
    numbers.append(N[idx+1] - N[idx])

gcd = N[1] - N[0]

for num in numbers:
    gcd = math.gcd(gcd, num)

result = [gcd] # gcd는 미리 추가해 놓기

for i in range(2, int(gcd ** 0.5)+1): # 시간 초과 해결을 위해 sqrt(gcd) 까지만 검사
    if gcd % i == 0: # 약수들 추가하기
        result.append(i)
        result.append(gcd // i)


result = list(set(result))        
result.sort()
print(*result)