"""
BAEKJOON ALGORITHM
Date : 2022-01-14
Start Time : 10:51
End Time : 13:30
File Name : 1727 커플 만들기 (G3)
URL : https://www.acmicpc.net/problem/1727
Category : Sorting
"""

n, m = map(int, input().split())

Male = list(map(int, input().split()))      # 남자들의 성격을 저장하는 리스트
Female = list(map(int, input().split()))    # 여자들의 성격을 저장하는 리스트

if n > m:   # n(원래 Male 자리)이 무조건 수가 적은 성별로 고정
    Male, Female = Female, Male
    n, m = m, n
    
result = [[0 for _ in range(m)] for _ in range(n)] # result matrix 초기화

Male.sort()
Female.sort()

result[0][0] = abs(Male[0] - Female[0])
for i in range(1, m - n + 1):  # result matrix 생성
    result[0][i] = min(abs(Male[0] - Female[i]), result[0][i-1])

for i in range(1, n):
    for j in range(i, m - (n - i - 1)):
        if i == j:
            result[i][j] = result[i-1][j-1] + abs(Male[i] - Female[j])
        else:
            result[i][j] = min(result[i][j-1], result[i-1][j-1] + abs(Male[i] - Female[j]))    # min 앞부분은 i가 더 작은경우, 뒷부분은 j가 더 작은경우

print(result[n-1][m-1])