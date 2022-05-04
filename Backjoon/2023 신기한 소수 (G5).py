"""
BAEKJOON ALGORITHM
Date : 2022-05-04
Start Time : 20:46 / 21:36
End Time : 21:05 / 21:42
File Name : 2023 신기한 소수 (G5)
Category : Mathematics
"""

# 첫 번째 자리에는 {2, 3, 5, 7}이 올 수 있으며,
# 그 외의 자리에는 {1, 3, 7, 9}가 올 수 있다.

def Stange_Prime_Number(number):
    for n in range(2, int(number ** 0.5) + 1):
        if number % n == 0:
            return
        
    if 10**(N-1) <= number < 10**N:
        print(number)
        return
        
    for other in OTHERS:
        Stange_Prime_Number(number*10 + int(other))

N = int(input())

FIRST = ("2", "3", "5", "7")
OTHERS = ("1", "3", "7", "9")

for F in FIRST:
    Stange_Prime_Number(int(F))