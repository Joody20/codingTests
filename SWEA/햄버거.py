for test_case in range(1, T+1):
    N , L = map(int, input().split())
    score_calories = [list(map(int,input().split())) for _ in range(N)]

    dp = [-1] * (L + 1)  # dp[c]는 c 칼로리에서 얻을 수 있는 최대 맛 점수를 저장
    dp[0] = 0  # 칼로리가 0일 때는 맛 점수도 0 (아무 재료도 사용하지 않음)

    # 각 재료를 순차적으로 처리
    for taste, calories in score_calories:
        # dp 배열을 뒤에서부터 갱신하는 이유는 중복된 재료를 사용하지 않도록 하기 위함
        for c in range(L, calories - 1, -1):
            if dp[c - calories] != -1:  # 이전 칼로리 값이 유효하면
                dp[c] = max(dp[c], dp[c - calories] + taste)  # 새로운 맛 점수를 갱신

        # 결과는 칼로리 제한 이하에서 얻을 수 있는 최대 맛 점수
    max_score = max(dp)
        
    print(f"#{test_case} {max_score}")