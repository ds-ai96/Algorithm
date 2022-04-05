"""
BAEKJOON ALGORITHM
Date : 2022-04-05
Start Time : 12:15
End Time : 12:34
File Name : 16193 차이를 최대로 2
URL : https://www.acmicpc.net/problem/16193
Category : Mathematics
"""

from collections import deque

N = int(input())
# 숫자들을 덱으로 생성(앞/뒤에서 숫자 빼야해서 리스트보다는 덱이 편함)
numbers = list(map(int, input().split()))
numbers.sort()
numbers = deque(numbers)

result_list = deque() # 정렬된 결과 수열 저장하는 덱
result_list.append(numbers.pop()) # 숫자들 중 가장 큰 숫자 빼기

result = 0 # 정렬된 덱으로 계산했을 때 결과값

for idx in range(N-1): # 미리 하나를 빼서 N-1까지
    # numbers의 가장 양 끝 수와 result_list의 양 끝을 비교해서 numbers의 수를 result_list의 어디에 넣을 지 정한다.
    
    tmp1 = abs(numbers[-1] - result_list[-1]) # number가장 큰 수 - result_list 가장 큰 수
    tmp2 = abs(numbers[-1] - result_list[0]) # number 가장 큰 수 - result_list 가장 작은 수
    tmp3 = abs(numbers[0] - result_list[-1]) # number 가장 작은 수 - result_list 가장 큰 수
    tmp4 = abs(numbers[0] - result_list[0]) # number 가장 작은 수 - result_list 가장 작은 수
    
    tmp = max(tmp1, tmp2, tmp3, tmp4) # 4가지 조건 중 최댓값 찾기
    
    if tmp == tmp1:
        result += tmp1
        result_list.append(numbers.pop())
        
    elif tmp == tmp2:
        result += tmp2
        result_list.appendleft(numbers.pop())
        
    elif tmp == tmp3:
        result += tmp3
        result_list.append(numbers.popleft())
        
    else:
        result += tmp4
        result_list.appendleft(numbers.popleft())

print(result)