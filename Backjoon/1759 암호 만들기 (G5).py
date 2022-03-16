"""
BAEKJOON ALGORITHM
Date : 2022-03-16
Start Time : 13:47
End Time : 14:11
File Name : 1759 암호 만들기 (G5)
URL : https://www.acmicpc.net/problem/1759
Category : 	Bruteforcing
"""
import sys
from itertools import combinations

L, C = map(int, sys.stdin.readline().split())

possible_word = sorted(list(sys.stdin.readline().split())) # 암호를 알파벳 증가하는 순으로 생성하기 위해 미리 정렬
passwords = [] # 가능한 암호들을 저장하는 배열

vowels = ["a", "e", "i", "o", "u"]

for combination in combinations(possible_word, L):
    consonant = vowel = 0 # 자음과 모음의 갯수
    for char in list(combination): # 생성된 암호에 자음 & 모음 갯수 확인하기
        if char in vowels: vowel += 1
        else: consonant += 1
    
    if vowel >= 1 and consonant >= 2: # 자음이 2개 이상 & 모음이 1개 이상인 경우
        passwords.append("".join(combination))
        
for password in passwords:
    print(password)