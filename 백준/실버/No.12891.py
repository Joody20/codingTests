"""
백준 실버 2 DNA 비밀번호 : https://www.acmicpc.net/problem/12891

평소에 문자열을 가지고 노는 것을 좋아하는 민호는 DNA 문자열을 알게 되었다. DNA 문자열은 모든 문자열에 등장하는 문자가 {‘A’, ‘C’, ‘G’, ‘T’} 인 문자열을 말한다. 예를 들어 “ACKA”는 DNA 문자열이 아니지만 “ACCA”는 DNA 문자열이다. 이런 신비한 문자열에 완전히 매료된 민호는 임의의 DNA 문자열을 만들고 만들어진 DNA 문자열의 부분문자열을 비밀번호로 사용하기로 마음먹었다.

하지만 민호는 이러한 방법에는 큰 문제가 있다는 것을 발견했다. 임의의 DNA 문자열의 부분문자열을 뽑았을 때 “AAAA”와 같이 보안에 취약한 비밀번호가 만들어 질 수 있기 때문이다. 그래서 민호는 부분문자열에서 등장하는 문자의 개수가 특정 개수 이상이여야 비밀번호로 사용할 수 있다는 규칙을 만들었다.

임의의 DNA문자열이 “AAACCTGCCAA” 이고 민호가 뽑을 부분문자열의 길이를 4라고 하자. 그리고 부분문자열에 ‘A’ 는 1개 이상, ‘C’는 1개 이상, ‘G’는 1개 이상, ‘T’는 0개 이상이 등장해야 비밀번호로 사용할 수 있다고 하자. 이때 “ACCT” 는 ‘G’ 가 1 개 이상 등장해야 한다는 조건을 만족하지 못해 비밀번호로 사용하지 못한다. 하지만 “GCCA” 은 모든 조건을 만족하기 때문에 비밀번호로 사용할 수 있다.

<민호가 만든 임의의 DNA 문자열과 비밀번호로 사용할 부분분자열의 길이, 그리고 {‘A’, ‘C’, ‘G’, ‘T’} 가 각각 몇번 이상 등장해야 비밀번호로 사용할 수 있는지 순서대로 주어졌을 때 민호가 만들 수 있는 비밀번호의 종류의 수를 구하는 프로그램을 작성하자. 단 부분문자열이 등장하는 위치가 다르다면 부분문자열이 같다고 하더라도 다른 문자열로 취급한다.>

첫 번째 줄에 민호가 임의로 만든 DNA 문자열 길이 |S|와 비밀번호로 사용할 부분문자열의 길이 |P| 가 주어진다. (1 ≤ |P| ≤ |S| ≤ 1,000,000)

두번 째 줄에는 민호가 임의로 만든 DNA 문자열이 주어진다.

세번 째 줄에는 부분문자열에 포함되어야 할 {‘A’, ‘C’, ‘G’, ‘T’} 의 최소 개수가 공백을 구분으로 주어진다. 각각의 수는 |S| 보다 작거나 같은 음이 아닌 정수이며 총 합은 |S| 보다 작거나 같음이 보장된다.

첫 번째 줄에 민호가 만들 수 있는 비밀번호의 종류의 수를 출력해라.

예제 1
9 8
CCTGGATTG
2 0 1 1

출력 1
0

예제 2
4 2
GATA
1 0 0 1

출력 2
2

"""

from collections import Counter
import sys
sys.stdin = open("input.txt")

s,p = map(int,input().split())  # s는 민호가 임의로 만든 DNA 문자열 길이 , p는 부분 문자열의 길이
dna_str = input()

least = list(map(int,input().split()))  # {‘A’, ‘C’, ‘G’, ‘T’} 의 최소 개수가 공백을 구분
alpha = ['A', 'C', 'G', 'T'] 

"""
# ver 1
dict = {}  # {‘A’, ‘C’, ‘G’, ‘T’} 와 최소개수 딕셔너리 형태로 저장

count = 0
for l in range(len(least)):
    dict[alpha[l]] = least[l]

for i in range(s-p+1):
    window = dna_str[i:i+p]
    window_count = Counter(window)

    # 모든 알파벳 개수가 최소 개수와 맞는지를 체크해야해.
    check = True
    for key in dict:
        if window_count[key] < dict[key]:
            check = False
            break

    if check:
        count += 1

print(count)
"""

# ver 2
check = dict(zip(alpha, least))  # 알파벳 최소 개수 딕셔너리
answer = 0

#두개의 포인터 지정
i = 0
j = p - 1

current = {'A' : 0, 'C': 0 , 'G': 0, 'T': 0}  # 현재 윈도우 상태
targetStr = dna_str[i:j]  # p의 개수만큼 잘라

for item in targetStr:  # 자른거에
    current[item] += 1  # 현재 윈도우 상태를 업데이트 해주는거야.

# 슬라이딩 윈도우
while j <= s-1:  # dna문자열 길이까지 되면,

    # 인덱스 초과 나니까 j+=1 하기 전에, 오른쪽 원소 추가하는 로직 먼저
    current[dna_str[j]] += 1

    # 비밀번호 유효성 검사
    if current['A'] >= least[0] and current['C'] >= least[1] and current['G'] >= least[2] and current['T'] >= least[3]:
        answer += 1

    current[dna_str[i]] -= 1  # 맨 왼쪽 원소 빼줌.
    i += 1
    j += 1

print(answer)