for test_case in range(1, 11):
    N = int(input()) # 건물의 개수 
    height_list = list(map(int, input().split())) # 건물의 높이

    count = 0

    for i in range(N):
        if 1 < i < N-2:
            if (height_list[i] > max(height_list[i-1], height_list[i-2], height_list[i+1],height_list[i+2])):
                count += height_list[i] - max(height_list[i-1], height_list[i-2], height_list[i+1],height_list[i+2])
    print(f"{test_case} {count}")
