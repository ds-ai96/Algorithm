"""
BAEKJOON ALGORITHM
Date : 2021-12-30
Start Time : 11:33
End Time : 11:42
File Name : 1316 그룹 단어 체커 (S5)
Category : Implementation
"""

N = int(input())
count = 0

for _ in range(N):
    word = list(input())
    result = []
    tmp = 0
    for w in word:
        
        if tmp != w:
            result.append(w)
        tmp = w    
        
    if len(result) == len(set(result)):
        count += 1
            
print(count)