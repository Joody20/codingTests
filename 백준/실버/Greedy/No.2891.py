"""
백준 카약과 강풍 : https://www.acmicpc.net/problem/2891

2890번을 보면 알겠지만, 상근이는 카약 대회를 개최했다. 그런데, 갑자기 엄청난 강풍이 경기장에 불었고, 일부 카약이 부서졌다. 경기는 5분 안에 시작해야 하는 상황이다.

다행히 일부 팀은 혹시 모를 사태에 대비해서 카약을 하나 더 경기장에 들고 왔다. 카약은 매우 무겁고 운반하기 어렵다. 따라서, 자신의 바로 다음이나 전에 경기하는 팀에게만 카약을 빌려주려고 한다. 즉, 팀 4는 여분의 카약을 3이나 5에게만 빌려줄 수 있다. 다른 팀에게서 받은 카약은 또 다른 팀에게 빌려줄 수 없다. 또, 카약을 하나 더 가져온 팀의 카약이 손상되었다면, 여분의 카약으로 경기에 출전하게되고, 이 카약은 다른 팀에게 빌려줄 수 없다.

카약이 부서진 팀과 하나 더 가져온 팀이 주어진다. 카약을 적절히 빌렸을 때 출발하지 못하는 팀의 최솟값은 몇 팀인지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 팀의 수 N, 카약이 손상된 팀의 수 S, 카약을 하나 더 가져온 팀의 수 R이 주어진다. (2 ≤ N ≤ 10, 1 ≤ S, R ≤ N)

둘째 줄에는 카약이 손상된 팀의 번호가 주어진다. 팀 번호는 중복되지 않는다.

셋째 줄에는 카약을 하나 더 가져온 팀의 번호가 주어진다. 팀 번호는 중복되지 않는다.

첫째 줄에 출발을 할 수 없는 팀의 최솟값을 출력한다.

예제 1
5 2 1
2 4
3

출력 1
1

예제 2
5 2 3
2 4
1 3 5

출력 2
0

"""

import sys
sys.stdin = open("input.txt","r")

N, S, R = map(int,input().split())  # N:팀의수, S : 손상된 카약 수, R:하나더 챙긴 팀의 수
broken = set(map(int,input().split()))
onemore = set(map(int,input().split()))


#하나 더 챙긴 팀의 카약이 부서질 경우 다른 팀에게 빌려줄 수 없기 때문에,
# 이 로직을 구현했어야 했음.
intersect = broken & onemore  # 아 이거 교집합을 뜻한데, 카약이 부서진 팀과 하나더 챙겨온 팀인 거를 구하기 위해.
broken -= intersect  # 부서진 팀 중에서 자기 여분으로 해결 가능한 팀은 더 이상 "문제 있는 팀"이 아니므로 제거
onemore -= intersect  # 하나 더 챙겨줄 수가 없어서 빼주는거임. -> 빌려줄 수 있는 여분에서 제거

for i in sorted(onemore):
    if i-1 in broken:
        broken.remove(i-1)
    elif i+1 in broken:
        broken.remove(i+1)
print(len(broken))



"""
break_kayak = list(map(int,input().split()))  # 손상된 카약 팀 번호
onemore = list(map(int,input().split()))  # 하나 더 챙긴 팀 번호


# 하나 더 챙긴 팀 번호 -1,+1이 break_kayak에 있으면, 둘 중 첫번째 것만 pop
cnt = 0
# 근데 손상된 카약의 수 보다 하나 더 챙긴 팀의 수가 더 많으면 0을 리턴
if S < R:
    print(0)
else: # 하나 더 챙긴 팀의 수 보다 손상된 카약이 더 많은 경우
    for i in range(R):
        if (onemore[i]+1 in break_kayak) or (onemore[i]-1 in break_kayak):
            cnt += 1      
    print(cnt)

"""