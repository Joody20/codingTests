for test_case in range(1,11):
    n = int(input())
    print(f'#{n}', end=' ')


    Array  = [list(map(int, input().split())) for _ in range(100)] # 이건 이제 2차원의 배열 형태로 받아옴.
    Array_r = list(zip(*Array))  # 이렇게 하면 행과열이 바뀐 list로 저장이 되는거임.

    ans = []
    digonal_lsum = 0
    digonal_rsum = 0
    # 좌측 대각선 합
    for i in range(len(Array)):
        digonal_lsum += Array[i][i]
    # 우측 대각선 합
    for j in range(len(Array)):
        num = len(Array) - j - 1 # 열 인덱스
        digonal_rsum += Array[j][num]

    ans.append(digonal_lsum)
    ans.append(digonal_rsum)
    # print(len(ans))


    for i in range(len(Array)):
        row = sum(Array[i])  # 가로의 합
        col = sum(Array_r[i]) # 세로의 합

        ans.append(row)
        ans.append(col)

    print(max(ans))