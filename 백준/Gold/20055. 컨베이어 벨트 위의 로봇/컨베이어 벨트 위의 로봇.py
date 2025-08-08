from collections import deque

N, K = map(int,input().split())
insides = deque(map(int,input().split())) # A_i의 내구도


result = 0
robots = deque([0] * N)  # 로봇의 유무를 알기 위한 deque


while True:

    result += 1

    # 1. 한칸 씩 회전
    insides.rotate(1) # rotate안에 숫자가 양수이면 오른쪽으로 양수의 수 만큼 회전, 음수이면 왼쪽으로 음수의 수만큼 회전
    robots.rotate(1)
    robots[-1] = 0  # 내리는 위치(N-1)에 도달할 경우 즉시 내림. 즉, 끝에 도달할 경우 즉시 내림

    # 2. 로봇 이동하기 -> 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1이상있어야돼.
    for i in range(N-2, -1, -1):  # 뒤에서 앞으로 순회
        if insides[i+1] >= 1 and robots[i+1] == 0 and robots[i] == 1:
            robots[i+1] = 1 # 로봇 이동
            robots[i] = 0  # 로봇 전 위치 로봇 사라짐.
            insides[i+1] -= 1 # 로봇이 어떤 칸으로 이동하면 그 칸의 내구도는 즉시 1만큼 감소한다.

    robots[-1] = 0  # 이동 후에도 내리는 위치에 도달할 경우 즉시 내림.


    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올리고, 내구도 감소
    if insides[0] != 0 and robots[0] != 1:
        robots[0] = 1 # 로봇 올리고
        insides[0] -= 1 # 내구도 감소

    # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    if insides.count(0) >= K:
        break


print(result)
