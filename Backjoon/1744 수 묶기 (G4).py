"""
BAEKJOON ALGORITHM
Date : 2022-03-24
Start Time : 11:59
End Time : 12:23
File Name : 1744 수 묶기 (G4)
URL : https://www.acmicpc.net/problem/1744
Category : Sorting
"""

N = int(input())

numbers = [int(input()) for _ in range(N)]

pos_numbers = []
neg_numbers = []
result = 0

for num in numbers:
    if num > 1:
        pos_numbers.append(num)
    elif num == 1: # 1은 곱하는 것 보다 더하는 것이 무조건 이득
        result += 1
    else: # 0은 음수랑 곱해져서 0으로 만드는 것이 이득이기 때문에 neg_numbers로 넣는다.
        neg_numbers.append(num) 
        
pos_numbers.sort(reverse=True) # 오름차순으로 정렬
neg_numbers.sort() # 내림차순으로 정렬 (절댓값이 오름차순으로 되게)


# 양수 더하기
for idx in range(len(pos_numbers) // 2):
    result += (pos_numbers[2 * idx] * pos_numbers[2*idx + 1])

if (len(pos_numbers) % 2 == 1) and (len(pos_numbers) != 0):# pos_numbers의 길이가 홀수인 경우
    result += pos_numbers[-1]
        
# 음수 더하기        
for idx in range(len(neg_numbers) // 2):
    result += (neg_numbers[2 * idx] * neg_numbers[2*idx + 1])
    
if (len(neg_numbers) % 2 == 1) and (len(neg_numbers) != 0):
        result += neg_numbers[-1]
    
print(result)