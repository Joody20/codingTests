"""
백준 단축키 지정(실버 1) : https://www.acmicpc.net/problem/1283

한글 프로그램의 메뉴에는 총 N개의 옵션이 있다. 각 옵션들은 한 개 또는 여러 개의 단어로 옵션의 기능을 설명하여 놓았다. 그리고 우리는 위에서부터 차례대로 각 옵션에 단축키를 의미하는 대표 알파벳을 지정하기로 하였다. 단축키를 지정하는 법은 아래의 순서를 따른다.

먼저 하나의 옵션에 대해 왼쪽에서부터 오른쪽 순서로 단어의 첫 글자가 이미 단축키로 지정되었는지 살펴본다. 만약 단축키로 아직 지정이 안 되어있다면 그 알파벳을 단축키로 지정한다.
만약 모든 단어의 첫 글자가 이미 지정이 되어있다면 왼쪽에서부터 차례대로 알파벳을 보면서 단축키로 지정 안 된 것이 있다면 단축키로 지정한다.
어떠한 것도 단축키로 지정할 수 없다면 그냥 놔두며 대소문자를 구분치 않는다.
위의 규칙을 첫 번째 옵션부터 N번째 옵션까지 차례대로 적용한다.

첫째 줄에 옵션의 개수 N(1 ≤ N ≤ 30)이 주어진다. 둘째 줄부터 N+1번째 줄까지 각 줄에 옵션을 나타내는 문자열이 입력되는데 하나의 옵션은 5개 이하의 단어로 표현되며, 각 단어 역시 10개 이하의 알파벳으로 표현된다. 단어는 공백 한 칸으로 구분되어져 있다.

N개의 줄에 각 옵션을 출력하는데 단축키로 지정된 알파벳은 좌우에 [] 괄호를 씌워서 표현한다.

예제 1                  출력 1
5                   
New                    [N]ew              
Open                   [O]pen
Save                   [S]ave
Save As                Save [A]s
Save All               Sa[v]e All
"""
import sys
sys.stdin = open("input.txt","r")

N = int(input())  # 옵션의 개수

options = [input().split() for _ in range(N)]


ops = [] # 단축키 지정 배열

for op in options:
    flag = False
    
    for i in range(len(op)):
        if op[i][0].upper() not in ops:
            ops.append(op[i][0].upper())
            flag = True
            op[i] = '[' + op[i][0] + ']' + op[i][1:]
            print(' '.join(op))
            break

    if not flag:
        for i in range(len(op)):
            check = False
            for j in range(len(op[i])):
                if op[i][j].upper() not in ops:
                    ops.append(op[i][j].upper())
                    flag = True
                    check = True
                    op[i] = op[i][:j] + '[' + op[i][j] + ']' + op[i][j+1:]
                    print(' '.join(op))
                    break
            if check:
                break

    if not flag:  # 아예 ops에 다 들어가져 있어서 단축키 지정이 안되는 경우 그냥 word 출력
        print(' '.join(op))




    # for i in range(len(op)):
    #     if op[0][0] in ops:   # 첫글자가 ops안에 있고
    #         if op[1][0] in ops:  # 그 다음 글자 첫글자도 ops에 있으면
    #             if op[0][i+1] in ops:
    #                 ops.append(op[0][i+2])  # 첫글자 두번째 글자도 ops에 있으면 첫글자 다다음글자로
    #         else:
    #             ops.append(op[1][0])
    #     else:
    #         ops.append(op[0][0])




