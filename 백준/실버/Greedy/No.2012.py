import sys
sys.stdin = open("input.txt","r")

N = int(input())
prides = []
for _ in range(N):
    pride = int(input())
    prides.append(pride)

pride = sorted(prides)  # 예상 등수를 오름차순으로 정렬해줌.

min_sum = 0
for i , p in enumerate(pride):
    min_sum += abs((i+1) - p)
print(min_sum)