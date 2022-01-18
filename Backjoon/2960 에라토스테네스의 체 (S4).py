"""
BAEKJOON ALGORITHM
Date : 2021-12-29
Start Time : 20:48
End Time : 21:14
File Name : 2960 에라토스테네스의 체 (S4)
Category : Implementation
"""

N, K = map(int, input().split())

num = [1 for _ in range(2, N+3)]
cnt = 0

for i in range(2, len(num)):
    for j in range(i, len(num), i):
        if num[j] == 1:
            num[j] = 0

            cnt += 1
            if cnt == K:
                print(j)
                break