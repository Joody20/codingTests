T = int(input())

for _ in range(1,T+1):
    H,W,N = map(int,input().split())

    nums = []

    for i in range(1,H+1):
        Y = 100 * i

        for j in range(1,W+1):
            XX = Y + j

            nums.append(XX)

    nums = sorted(nums, key=lambda x : (x % 100, x))

    print(nums[N-1])