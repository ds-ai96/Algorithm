"""
BAEKJOON ALGORITHM
Date : 2022-04-15
Start Time : 11:38
End Time : 12:11
File Name : 2824 최대공약수 (G5)
URL : https://www.acmicpc.net/problem/2023
Category : Mathematics
"""

def GCD(numA, numB):
    while numB > 0:
        tmp = numA % numB
        numA, numB = numB, tmp
    return numA

A = int(input())
numAs = list(map(int, input().split()))

B = int(input())
numBs = list(map(int, input().split()))

numA = 1
numB = 1

for num in numAs:
    numA *= num
    
for num in numBs:
    numB *= num
    
result = GCD(numA, numB)
print(str(result)[-9:])