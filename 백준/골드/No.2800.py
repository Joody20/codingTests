"""
백준 골드4(자료구조) 괄호제거 : https://www.acmicpc.net/problem/2800

예제1
(0/(0))
예제2
(2+(2*2)+2)
예제3:
(1+(2*(3+4)))

출력
올바른 괄호 쌍을 제거해서 나올 수 있는 서로 다른 식을 사전 순으로 출력한다.
https://velog.io/@leetaekyu2077/%EB%B0%B1%EC%A4%80-2800%EB%B2%88-%EA%B4%84%ED%98%B8-%EC%A0%9C%EA%B1%B0 -> 참고

"""

from itertools import combinations
import sys
sys.stdin = open("input.txt","r")

string = list(input())
indices = []
stack = []
ans = set()

for i in range(len(string)):
    if string[i] == '(':
        stack.append(i)
    elif string[i] == ')':  # 올바른 괄호일 때의 인덱스를 저장해놈..
        indices.append((stack.pop(), i)) # stack에서 pop한거 그 위치를 append하는거임.

for i in range(len(indices)):
    for comb in combinations(indices, i+1): # combinations(조합하고자 하는 요쇼들이 저장된 리스트들 , 한 조합의 길이)
        temp = string[:]
        for idx in comb:
            temp[idx[0]] = temp[idx[1]] = ""

        ans.add("".join(temp))


for item in sorted(list(ans)):
    print(item)

# print(string)
# print(temp)
# print(ans)