"""
BAEKJOON ALGORITHM
Date : 2022-04-07
Start Time : 13:36
End Time : 15:08
File Name : 23848 등비수열의 합 (G3)
URL : https://www.acmicpc.net/problem/23848
Category : Bruteforcing
"""
import sys
import math

N = int(sys.stdin.readline().rstrip())

divisor = []

for num in range(1, int(N**0.5)):
    if N % num == 0:
        divisor.append(num)
        divisor.append(N//num)

divisor.sort()

# for a in range(1, N+1): # 조건 1: 1~N : N의 약수의 범위 (a는 N의 약수이다)
#     if a * a > N: break # a는 N의 약수가 아닌 조건
#     if N % a: continue # a가 N의 약수가 아니라면, a+1을 해서 다시 진행
for a in divisor:    
    for n in range(3, 40): # 조건 2: a=1, r=2인 경우 n은 40보다 작아야 한다.
        low, high = 2, int(1e6) # 조건 3: a=1, n=3인 경우 r은 1e6보다 작아야 한다.
        
        # 적당한 r을 찾기위해 이진 탐색 진행
        while low+1 < high:
            
            mid = low + high >> 1

            
            if a * (math.pow(mid, n) - 1) <= N * (mid - 1): low = mid # N보다 작은 경우 mid를 더 크게 만들어야 한다.
            else: high = mid # N보다 큰 경우 mid를 더 작게 만들어야 한다.
        
        if int(a * (math.pow(low, n) - 1) / (low-1)) == N:
            print(n)
            print(*[a * int(math.pow(low, i)) for i in range(n)])
            exit(0)
            
print(-1)