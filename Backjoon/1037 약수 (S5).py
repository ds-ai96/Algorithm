"""
BAEKJOON ALGORITHM
Date : 2022-02-15
Start Time : 19:29
End Time : 19:37
File Name : 1037 약수 (S5)
Category : Mathematics
"""

N = int(input())
numbers = list(map(int, input().split()))

print(max(numbers) * min(numbers))