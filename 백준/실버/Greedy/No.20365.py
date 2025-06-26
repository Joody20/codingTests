import sys
sys.stdin = open("input.txt","r")


N = int(input())
colors = input()

cnt_B = 1
cnt_R = 1


if colors[0] == 'B':
    cnt_B += 1

else:
    cnt_R += 1

for i in range(1,N):
    if colors[i] != colors[i-1]:
        if colors[i] == 'B':
            cnt_B += 1
        else:
            cnt_R += 1


print(min(cnt_B, cnt_R))
