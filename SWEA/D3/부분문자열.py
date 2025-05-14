import sys
sys.stdin = open("input.txt","r")

"""
길이가 K인 문자열 S가 있을 때, S의 연속된 일부분을 부분 문자열이라고 한다.

부분 문자열은 원래의 순서가 바뀌거나 중간에 있는 글자가 빠져서는 안된다.

주어진 문자열의 부분 문자열을 사전순으로 정렬한 후, N번째 부분 문자열의 첫 글자와 글자 수를 출력하는 프로그램을 완성하시오.

예를 들어 abac의 부분 문자열은 사전순으로 정렬하면 다음과 같다.

a ab aba abac ac b ba bac c

3번째 부분 문자열은 aba가 된다.


[입력]

첫 줄에 테스트 케이스의 개수 T가 주어지고, 다음 줄부터 각 줄에 N과 문자열이 주어진다.

문자열의 길이는 4글자 이상 1000글자 이내이고, N은 문자열의 길이 이내이다. ( 1<=T<=50 )

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.

예제 1
3
5 abac
9 ltsodjxzyc
21 jldgovukjf

출력 1

#1 a 2
#2 j 2
#3 j 4

"""
# 방법 1
from collections import defaultdict
T = int(input())

for t in range(T):
    N , S = input().split()
    n = int(N)
    s = len(S)

    substrings = defaultdict(list)  # defaultdict는 키가 없을 때 자동으로 기본값을 생성해주는 딕셔너리예요.
    for i, ch in enumerate(S):  # S의 인덱스와, 문자가 나와
        substrings[ch].append(i) # 문자에 대한 인덱스를 substrings에 넣어줌.


    sorted_substr = dict(sorted(substrings.items()))  # 문자 기준으로 정렬

    result = []  # 중복 없는 부분문자열들을 넣어줄거야.
    for j in sorted_substr:    # 사전순으로 정렬된 문자순으로 출력하고,
        for idx in sorted_substr[j]:  # 그 문자의 인덱스를 출력하고,
            for k in range(idx + 1, s + 1): # 인덱스 idx부터 시작해서 가능한 모든 연속된 부분 문자열을 만듦.
                if S[idx:k] not in result:   # result에 연속된 부분 문자열이 없으면
                    result.append(S[idx:k])  # result에 그 부분 문자열을 넣어줌.

        if len(result) >= n:
            break


    sorted_result = sorted(result)
    nth_str = sorted_result[n-1]  # n번 째 부분문자열을 가져옴.

    print(f"#{t+1} {nth_str[0]} {len(nth_str)}")  # n번째 부분문자열의 첫글자와, 글자수를 리턴함.



#방법 2
# T= int(input())

# for t in range(T):
#     N , inputs = input().split()

#     n = int(N)

#     substrings = set()  # 중복 방지 set으로 해줌..

#     for i in range(len(inputs)):
#         for j in range(i+1, len(inputs) + 1):
#             substrings.add(inputs[i:j])

#     nth_string = sorted(substrings)[n-1]

#     print(f"#{t+1} {nth_string[0]} {len(nth_string)}")


