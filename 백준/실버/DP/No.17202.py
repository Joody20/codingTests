"""
백준 핸드폰 번호 궁합(브론즈 1) : https://www.acmicpc.net/problem/17202


"""

import sys
sys.stdin = open("input.txt","r")

A = list(map(int,input()))
B = list(map(int,input()))

AB = []

for a,b in zip(A,B):
    AB.append(a)
    AB.append(b)


while len(AB) > 2:
    dp = []
    for i in range(len(AB)-1):
        dp.append((AB[i] + AB[i+1]) % 10)
    AB = dp

for i in AB:
    print(i,end='')
    
print()
    

