import sys
sys.stdin = open("input.txt", "r")

N = int(input())

num = list(map(int,input()))

res = 0

for n in num:
    res += n
print(res)