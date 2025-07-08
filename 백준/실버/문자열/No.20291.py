"""
백준 실버 3(문자열) : 파일 정리
https://www.acmicpc.net/problem/20291

예제
8
sbrus.txt
spc.spc
acm.icpc
korea.icpc
sample.txt
hello.world
sogang.spc
example.txt
"""

from collections import Counter
import sys
sys.stdin = open("input.txt", "r")

N = int(input())

extensions = [input().rstrip() for _ in range(N)]

count = 0 # 파일의 개수를 세는

res = [] # 정리한 확장자들을 넣는 

i = 0 # 현재 위치

for ex in extensions:  # 확장자들을 가져와서
    zum = ex.find(".",i) + 1  # 일단 점의 위치를 파악하고

    extension = str(ex[zum:])  # 확장자 이름을 가져왔어

    res.append(extension) # 새로운 배열 res에 확장자 이름을 넣어주고


cnt = Counter(res) # Counter을 이용해서 확장자들의 개수를 세어줬어

data = sorted(cnt.items()) # 사전순으로 나열했고


for item in data:  # 이것들을 이제 출력 방식이 문자열이였어서
    print(f"{item[0]} {item[1]}") # 이렇게 해줫어


