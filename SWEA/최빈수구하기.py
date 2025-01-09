T = int(input())


for test_case in range(1, T + 1):
    N = int(input())

    score = list(map(int, input().split())) # 지금 list 형태로 해놨기 때문에 score[1]이면 첫번째 학생의 score인거야 
    score_check = [0] * 101   # 점수(0 ~ 100)에 해당하는 빈도수를 저장할 배열을 초기화합니다.
                              # 인덱스가 점수, 값이 그 점수의 빈도수를 의미합니다.

    max_count = 0  # 최빈수 값

    for i in range(1000):
        score_check[score[i]] += 1  # 1000명이니까 1000번의 비교가 되고 계속 1씩 더해가. 다음다음 해서 1000번째까지 반복해

    for j in range(101):  # 0점부터 100점까지 모든 점수를 확인하며 최빈값을 찾습니다.
        if score_check[j] == max(score_check): # 현재 점수의 빈도수가 최대 빈도수와 같다면
            if j > max_count: # 점수가 더 크다면 max_count를 업데이트합니다.
                max_count = j


    print(f"#{test_case} {max_count}") 