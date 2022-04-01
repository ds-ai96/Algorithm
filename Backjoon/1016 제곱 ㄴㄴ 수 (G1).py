"""
BAEKJOON ALGORITHM
Date : 2022-04-01
Start Time : 10:10
End Time : 10:57
File Name : 1016 제곱 ㄴㄴ 수
URL : https://www.acmicpc.net/problem/1016
Category : Mathematics
"""
min, max = map(int, input().split())

square_numbers_idx = [False] * (max-min+1) # min ~ max 사이의 범위만 표시
# square[0] = min, square[-1] = max
result = max - min + 1
    
for number in range(2, int(max**0.5) + 1):
    square = number ** 2
    
    for idx in range((((min-1)//square)+1)*square, max+1, square):
        if not square_numbers_idx[idx - min]:
            square_numbers_idx[idx - min] = True
            result -= 1

print(result)