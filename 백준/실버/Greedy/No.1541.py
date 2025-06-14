import sys
sys.stdin = open("input.txt","r")

input = input()

tokens = input.split('-')


#첫부분은 그냥 더하고
total = sum(map(int, tokens[0].split('+')))


# 나머지 부분은 다 더하고 빼기
for token in tokens[1:]:
    total -= sum(map(int,token.split('+')))


print(total)
    