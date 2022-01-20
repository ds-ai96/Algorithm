"""
BAEKJOON ALGORITHM
Date : 2022-01-20
Start Time : 10:38
End Time : 11:15
File Name : 15810 풍선 공장 (S2)
URL : https://www.acmicpc.net/problem/15810
Category : Binary Search
"""

N, M = map(int, input().split()) # 스태프의 수 N명, 만들어야 하는 풍선의 갯수 M개
A = list(map(int, input().split())) # N 명의 스태프가 각각 풍선을 만드는 데 걸리는 시간

start = 0; end = max(A) * M
result = float("inf")
if M > 0:
    while (start <= end):
        mid = (start + end) // 2 # 풍선을 전부 만드는 데 걸리는 시간
        count = sum([mid// x for x in A]) # mid 시간 동안 만들 수 있는 풍선의 갯수

        if count >= M:
            result = min(mid, result)
            end = mid - 1
        else:
            start = mid + 1

    print(result)

else:
    print(0)