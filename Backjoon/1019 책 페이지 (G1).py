"""
BAEKJOON ALGORITHM
Date : 2022-04-04
Start Time : 21:14
End Time : 21:37
File Name : 1019 책 페이지 (G1)
URL : https://www.acmicpc.net/problem/1019
Category : Mathematics
"""

N = int(input())

numbers = [0] * 10 # 0부터 9까지 숫자들 빈도

page = 1

while N != 0:
    while N % 10 != 9: # 끝자리 9로 맞추기
        for num in str(N):
            numbers[int(num)] += page
        N -= 1
        
    if N < 10:
        for idx in range(N+1):
            numbers[idx] += page
        numbers[0] -= page
        break
    
    else:
        for idx in range(10):
            numbers[idx] += (N // 10 + 1) * page
    numbers[0] -= page
    page *= 10
    N //= 10
            
for number in numbers:
    print(number, end=" ")