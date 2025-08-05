import sys
sys.stdin = open("input.txt","r")

"""
현대모비스에서 소프트웨어 아카데미 견학생을 모집한다고 한다. 이번 견학 활동은 모두 팀 단위로 진행되며 아래 두 조건을 모두 만족하는 팀만 소프트웨어 아카데미를 견학할 수 있다.

팀원이 두 명이다.
팀의 능력치가 
$M$ 이상이다. 팀의 능력치는 모든 팀원의 능력치를 합한 값이다.
Sogang ICPC Team 학회원 
$N$명이 견학을 희망한다. 학회장 동건이는 
$N$명으로 최대한 많은 팀을 만들어 견학을 보내고 싶다. 동건이가 최대 몇 팀이나 견학 보낼 수 있을지 구해보자.

입력
첫째 줄에 견학을 희망하는 학회원의 수 
$N$과 견학하는 팀의 최소 능력치를 나타내는 정수 
$M$이 공백으로 구분되어 주어진다. (
$1 \le N \le 100\,000$, 
$1 \le M \le 10^9$)

둘째 줄에 학회원 
$N$명의 능력치를 나타내는 
$N$개의 정수 
$a_1,a_2, \cdots, a_N$이 공백으로 구분되어 주어진다. (
$1 \le a_i \le 10^9$)

출력
첫째 줄에 동건이가 견학 보낼 수 있는 최대 팀 수를 출력한다.

예제 1
6 10
3 5 7 3 5 6

출력 1
2

예제 2
1 10
100

출력 2
0

"""
# 투포인터 + 정렬로 풀었어야 했어
N,M = map(int,input().split())
powers = list(map(int,input().split()))

powers.sort() # 오름차순으로 정렬해주고!
left = 0
right = N - 1
team = 0  # 만들 수 있는 팀의 개수

while left < right:
    total = powers[left] + powers[right]

    if total >= M:
        team += 1
        left += 1
        right -= 1  # 두 수 모두 사용

    else:
        left += 1  # 작은 수 늘려서 합의 크기 늘리기


print(team)







"""
from itertools import combinations

두번째 방법도 안돼..;;
if N == 1:
    print(0)

sets = set()

for a,b in combinations(powers,2):

    if a + b >= M:
        pair = tuple(sorted((a,b)))
        
        if pair in sets:
            sets.remove(pair)
        else:
            sets.add(pair)


print(len(sets))

"""



# powers.sort(reverse= True)

# sets = []
# team = 0

# summ = 0

# else: # N이 2이상인 경우
#     for a,b in combinations(powers,2):
#         summ = a + b

#         if summ >= M:
#             sets.append((a,b))

#         else: # 두 수를 더해도 M이 안넘는 게 있다면 걍 0리턴
#             print(0)

    
# counts = Counter(sets)

# for pair in sets:
#     if counts[pair] == 1:
#         team += 1

# print(team)
        

    

