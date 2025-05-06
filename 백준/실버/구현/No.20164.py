import sys
sys.stdin = open("input.txt","r")
"""
백준 댄스파티 : http://acmicpc.net/problem/2831

문제
남자 N명과 여자 N명이 상근이가 주최한 댄스 파티에 왔다. 상근이는 모든 사람의 키를 알고있다. 각 남자는 모두 여자와 춤을 출 수 있고, 여자는 남자와 춤을 출 수 있다. 모든 사람은 많아야 한 사람과 춤을 출 수 있다.

모든 남자는 자신이 선호하는 여자와 춤을 추려고 한다. 각 남자가 선호하는 여자는 두 가지 유형이 있는데, 한 유형은 자신보다 키가 큰 여자이고, 다른 유형은 자신보다 키가 작은 유형이다. 여자도 남자와 마찬가지로 자신이 선호하는 남자와 춤을 추려고 한다. 각 여자가 선호하는 남자도 남자와 비슷하게 두 유형이 있다. (자신보다 키가 큰 남자, 작은 남자) 키가 같은 남자와 여자가 춤을 추는 일은 일어나지 않는다.

이때, 상근이는 각 사람의 키와 선호하는 이성 유형을 알고 있다. 이런 조건을 가지고 춤을 출 쌍을 만들어 주려고 한다. 상근이는 최대 몇 쌍을 만들 수 있을까?

입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100,000)

둘째 줄에는 남자의 키가 밀리미터 단위로 주어진다. 키는 절댓값이 1500보다 크거나 같고, 2500보다 작거나 같은 정수이다. 사람의 키는 주어지는 값의 절댓값이다. 키가 양수인 경우에는 자신보다 키가 큰 여자와 춤을 추기를 원하는 남자이고, 음수인 경우에는 키가 작은 사람과 춤을 추기를 원하는 남자이다.

셋째 줄에는 여자의 키가 밀리미터 단위로 주어진다. 키의 범위나 의미 역시 남자와 동일하다. 

출력
첫째 줄에 상근이가 만들어 줄 수 있는 쌍의 최댓값을 출력한다.

예제 1
1
-1800
1800
출력 1
0

예제 2
1
1700
-1800

출력 2
1

예제 3
2
-1800 -2200
1900 1700

출력 3
2

"""
N = int(input()) # 남,여 명수
M = list(map(int,input().split()))
W = list(map(int,input().split()))

M.sort()
W.sort()

couple = 0
i = 0
j = N-1

while i < N and 0<= j:  # 이거 i < N 이렇게 했어야 했어..
    if M[i] < 0 and 0 < W[j] and abs(M[i]) > W[j]:  # 남자키음수, 여자키양수, 남자키 > 여자키
        couple += 1
        i += 1
        j -= 1
    elif M[i] < 0 and 0 < W[j] and abs(M[i]) <= W[j]:  # 남자키음수, 여자키양수, 남자키 <= 여자키
        j -= 1
    elif 0 < M[i] and W[j] < 0 and M[i]  < abs(W[j]):  # 남자키양수, 여자키음수, 남자키 < 여자키
        couple += 1
        i+=1
        j -= 1
    elif 0 < M[i] and W[j] < 0 and M[i] >= abs(W[j]):
        j -= 1
    elif M[i] > 0 and W[j] > 0:
        j -= 1
    elif M[i] < 0 and W[j] < 0:
        i += 1

print(couple)




"""
men_short = []  # 남자는 키 작은 여자 선호
men_tall = []  # 남자는 키 큰 여자 선호
women_short = []  # 여자는 키 작은 남자 선호
women_tall = []  # 여자는 키 큰 남자 선호

# 남자와 여자의 키와 선호에 따라 분리
for m in M:
    if m < 0: # 남자의 키가 음수이면,
        men_short.append(abs(m))  # 키가 작은 여자를 선호
    else: # 양수이면,
        men_tall.append(abs(m))  # 키가 큰 여자 선호
for w in W:
    if w < 0:  # 여자의 키가 음수이면,
        women_short.append(abs(w))  # 키 작은 남자 선호
    else:    # 여자의 키가 양수이면,
        women_tall.append(abs(w))  # 키가 큰 남자 선호
 
couple = 0 # 커플의 쌍을 구해야함.

# 남자는 키 작은 여자를 선호함 -> 남자키 > 여자키 -> 여자는 키 큰 남자 선호
men_short.sort()
women_tall.sort()
# 투 포인터 사용
i=0
j=0

while i < len(men_short) and j < len(women_tall):
    if men_short[i] > women_tall[j]:
        couple += 1
        i += 1
        j += 1
    else:
        j += 1  # 똑같은 여자 선택하지 않게 j를 늘려줘.

# 남자는 키 큰 여자를 선호함 -> 남자키 < 여자키 -> 여자는 키 작은 남자 선호
men_tall.sort()
women_short.sort()
i=0
j=0
while i< len(men_tall) and j < len(women_short):
    if men_tall[i] < women_short[j]:
        couple += 1
        i += 1
        j += 1
    else:
        j += 1

print(couple)

"""