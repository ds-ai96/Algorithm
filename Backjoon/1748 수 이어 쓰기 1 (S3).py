"""
BAEKJOON ALGORITHM
Date : 2022-03-04
Start Time : 12:47
End Time : 13:15
File Name : 1748 수 이어 쓰기 1
URL : https://www.acmicpc.net/problem/1748
Category : Bruteforcing
"""

n = input()
length = len(n) - 1
result = 0

for i in range(length):
    result += 9 * (10 ** i) * (i + 1)

result += ((int(n) - (10 ** length)) + 1) * (length + 1)

print(result)