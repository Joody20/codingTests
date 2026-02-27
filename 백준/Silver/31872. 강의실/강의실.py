N , K = map(int,input().split())
times = sorted(list(map(int,input().split())))


gap = [times[0] - 0]


for i in range(N-1):
    gap.append(times[i+1] - times[i])


sorted_gap = sorted(gap,reverse=True)


print(sum(sorted_gap[K:]))