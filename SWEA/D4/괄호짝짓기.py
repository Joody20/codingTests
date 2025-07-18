import sys
sys.stdin = open("input.txt","r")

"""
4 종류의 괄호문자들 '()', '[]', '{}', '<>' 로 이루어진 문자열이 주어진다.

이 문자열에 사용된 괄호들의 짝이 모두 맞는지 판별하는 프로그램을 작성한다.

예를 들어 아래와 같은 문자열은 유효하다고 판단할 수 있다.

[입력]

각 테스트 케이스의 첫 번째 줄에는 테스트케이스의 길이가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.

총 10개의 테스트케이스가 주어진다.

181
(({<(({{[[[[<<[[(<[[{([{{{[<[[[{<<(<[[{}[]{}{}[]]]><<>{})[]{}><>[]<>><>}][]]<>{}]>]()}()()(){}}}{}][])(){}<>()}]{}[]]>()[][][]){}]]{}[]<>><>{}[]{}<>>]]]][]{}{}[]()}}))>}<>{}()))[][]

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 유효성 여부를 1 또는 0으로 표시한다 (1 - 유효함, 0 - 유효하지 않음).

#1 0
#2 0
#3 1
#4 1
#5 1
#6 0
#7 0
#8 1
#9 0
#10 1

"""

for t in range(1,11):
    N = int(input())
    arr = list(input())

    stack = []
    isValid = True

    pairs = {')':'(' , ']': '[' , '>':'<' , '}':'{'}


    for a in arr:
        if a in '([{<':
            stack.append(a)

        elif a in ')]}>':
            if not stack or stack[-1] != pairs[a]:
                isValid = False
                break
            stack.pop()

    if isValid and not stack:
        print(f"#{t} 1")
    else:
        print(f"#{t} 0")