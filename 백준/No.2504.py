def solution(s):
    stack = []  # 올바른괄호인지 올바르지 않은 괄호인지 판단하기 위한 스택
    num = 0 # 결과를 리턴할 숫자
    tmp = 1 # 중간과정을 계산할 숫자

    for i, char in enumerate(s):
        if(char == "("):  # 괄호가 열릴 때는 곱하고
            stack.append("(")
            tmp *= 2  # 일단 ( 이 괄호일 때는 2를 곱하는 거니까 일단 곱하고
        elif(char == ")"):  # 괄호가 닫힐 때는 나누고
            if not stack or stack[-1] != "(":
                return 0
            if s[i-1] == '(':  # 지금 전거가 (이면 num + tmp를 해
                num += tmp
            stack.pop()  # stack에서 빼고
            tmp //= 2  # 2를 나눠 
        elif(char == "["):
            stack.append("[")
            tmp *= 3  # 3을 곱하고
        elif(char == "]"):
            if not stack or stack[-1] != "[":
                return 0
            if s[i - 1] == '[':  #전거가 [이면 더하고
                num += tmp
            stack.pop()  # 빼주고
            tmp //= 3  # 나누고 
        else:
            return 0
    
    if stack:
        return 0
    
    return num

import sys
sys.stdin = open("input.txt", "r")  # 백준 문제 제출할 때는 이 두줄은 제외하고 제출하기 !
T = input().strip()
print(solution(T))