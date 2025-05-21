import sys
sys.stdin = open("input.txt","r")

"""
"기러기", "토마토", "스위스"와 같이 똑바로 읽어도 거꾸로 읽어도 똑같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.

8x8 평면 글자판에서 제시된 길이를 가진 회문의 개수를 구하라.

위와 같은 글자판이 주어졌을 때, 길이가 5인 회문은 붉은색 테두리로 표시된 4개이므로 4를 반환하면 된다.


[제약 사항]

각 칸의 들어가는 글자는 'A', 'B', 'C' 중 하나이다.

ABA도 회문이며, ABBA도 회문이다. A 또한 길이 1짜리 회문이다.

가로 또는 세로로 이어진 회문의 개수만 센다.

아래 그림에서 노란색 경로를 따라가면 길이 7짜리 회문이 되지만 직선이 아니기 때문에 인정되지 않는다.

[입력]

총 10개의 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 찾아야 하는 회문의 길이가 주어지며, 다음 줄에 8x8 크기의 글자판이 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 찾은 회문의 개수를 출력한다.

예제 1
4
CBBCBAAB
CCCBABCB
CAAAACAB
BACCCCAC
AABCBBAC
ACAACABC
BCCBAABC
ABBBCCAA
4
BCBBCACA
BCAAACAC
ABACBCCB
AACBCBCA
ACACBAAA
ACCACCCB
AACAAABA
CACCABCB
3
BABBBACB
ABCAACCB
CCACBCBA
CACACBCA
CCABACCB
CCBAAAAA
BBACBACA
CBCCBABC
4
ACBBCCCA
CCBCBACB
ACBCABAA
BABCCAAA
ACCCCCBB
AABBCCBC
CCABBACA
CAACBCCC
7
AAACACAB
CCABCCCC
CABCAAAA
BBBCBBBA
ABCCACCC
ABACBCBB
CBABACAB
BBBBBABB
3
ABCBCBCA
ABCBCCCB
ABACCCCA
BBABBBAC
BBACBCCC
AAACACCA
BABCCCBC
ACCBCBCA
7
CACBCCBA
CBCCBCCA
CCBCBCAB
BBCCABAA
CACCBCCC
BCCACCBB
CBCCCBBC
CBACBCBC
5
BCBABCBA
CBBABABC
BCACBAAA
BBABACAB
BCBCCBAC
CBBCBBBB
CBBAACAB
ACCBCBCC
3
BBBBCCAA
BCBBCACC
BBCAAAAB
ABABBABB
BACAAABA
ABACCBCA
ACCAABCB
BACCACBA
5
BCCCACCB
CABCACAB
BAACCCAC
BBABBABC
CCABABCA
CABABACC
CBACACAB
CBCCCBAB

출력 1
#1 12
#2 10
#3 31
#4 11
#5 1
#6 43
#7 2
#8 11
#9 34
#10 8

"""

for t in range(1,11):
    N = int(input())
    lst = [list(input()) for _ in range(8)]

    count = 0 # 호ㅣ문 개수

    #가로
    for i in range(8):
        for j in range(0, 8 - N + 1):  # 회문의 길이 만큼
            sub = lst[i][j:j+N]  # 가로는 한줄로 되어 있으니까 바로 슬라이싱이 가능함.
            if sub == sub[::-1]:
                count += 1

    #세로
    for i in range(8):
        for j in range(0, 8 - N + 1):
            sub = []
            for q in range(N):  # 세로는 직접 인덱스를 넣어줘야됌.
                sub.append(lst[j+q][i])
            if sub == sub[::-1]:
                count += 1

    print(f"#{t} {count}")
