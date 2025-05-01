import sys
sys.stdin = open("input.txt","r")

K = int(input())

# 최소한의 초콜릿 개수를 구함.
x  = 0
value = 1
while value < K:
    value *= 2
    x += 1

least_choco = pow(2,x)  # 2를 x번 곱해줌.

# least_choco가 K가 되기 위해 최소 몇번을 잘라야 하는지!
cnt = 0
temp = least_choco
if K != least_choco:   #K와 least_choco와 다르면
    while K:  # K가 0이 될 때까지
        temp //= 2 # temp를 2로 나누어주고
        if K >= temp:  # 아직 temp보다 K더 크다면,
            K = K - temp # 그만큼 빼주고,
            cnt += 1  # 쪼갠 수 cnt증가
        else:
            cnt += 1  # 쪼개기만 하기

print(least_choco, cnt)
