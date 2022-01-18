"""
BAEKJOON ALGORITHM
Date : 2022-01-17
Start Time : 11:40 
End Time : 11:58
File Name : 10815 숫자 카드 (S4)
URL : https://www.acmicpc.net/problem/10815
Category : Binary Search
"""
def binary_search(num_list, target, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    
    if target == num_list[mid]:
        return mid
    
    elif target > num_list[mid]:
        return binary_search(num_list, target, mid+1, end)
    
    else:
        return binary_search(num_list, target, start, mid-1)

N = int(input())
num_list = list(map(int, input().split()))

M = int(input())
target_list = list(map(int, input().split()))

num_list.sort()
result = []

for target in target_list:
    idx = binary_search(num_list, target, 0, N-1)
    if idx == -1:
        result.append(0)
    else:
        result.append(1)
        
for i in result:
    print(i, end=" ")