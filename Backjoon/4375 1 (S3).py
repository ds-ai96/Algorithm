"""
BAEKJOON ALGORITHM
Date : 2022-02-15
Start Time : 19:16
End Time : 19:26
File Name : 4315 1 (S3)
Category : Mathematics
"""
while True:
    try:
        n = int(input())
        result = '1'
        
        while True:
            if int(result) % n == 0:
                print(len(result))
                break
            result += "1"
        
    except EOFError:
        break