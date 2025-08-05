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