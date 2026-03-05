N = int(input())

wow = "WOW"

for _ in range(N):
    words = input()

    cnt = 0

    for i in range(len(words) - 2):
        if words[i:i+3] == wow:
           cnt += 1

    print(cnt)