"""
BAEKJOON ALGORITHM
Date : 2022-01-12
Start Time : 11:46
End Time : 12:08
File Name : 1263 시간 관리 (S1)
URL : https://www.acmicpc.net/problem/1263
Category : Sorting
"""

N = int(input())
work = []

for _ in range(N):
    work.append(list(map(int, input().split())))

work.sort(key=lambda x: x[1], reverse=True) # 가장 늦게 시작하는 시간이므로 거꾸로 생각

criteria = work[0][1] - work[0][0] # 제일 마감이 늦은 일을 제일 먼저 할당

for i in range(1, N):
    
    if criteria > work[i][1]: # 마감 시간에 여유가 있는 경우
        criteria = work[i][1] - work[i][0]
        
    else: # 마감 시간에 여유가 없는 경우
        criteria -= work[i][0]
        
print(criteria if criteria >= 0 else -1)