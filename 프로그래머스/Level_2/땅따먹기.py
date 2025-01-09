def solution(land):
    rows = len(land)
    cols = len(land[0])
    
    dp = [[0] * cols for _ in range(rows)] # rows와 cols에 맞게 0으로 맵핑된 dp를 하나 만들고
    
    for col in range(cols): # cols
        dp[rows-1][col] = land[rows-1][col] # 마지막 행은 그대로 dp에 복사

    
    for row in range(rows-2, -1, -1): # 마지막에서 두번째 줄 부터 시작
        for col in range(cols): # 현재 행의 모든 열을 순회
            # 다음 행에서 현재 열을 제외한 열 중 최대값을 찾음
            dp[row][col] = land[row][col] + max(dp[row + 1][next_col] for next_col in range(cols) if next_col != col)

    return max(dp[0])