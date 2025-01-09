for test_case in range(1,11): # 테스트 개수가 10개이니까 11까지 
    N = int(input()) # 회문 길이
    lst = [list(input()) for _ in range(8)]  # 알파벳들을 다 가져와 

    count = 0 # 회문 개수 count하는 변수

    # 가로
    for i in range(8): # 8x8 이니까 이렇게.
        for j in range(0, 8 - N + 1): # 회문의 길의 개수 N 만큼 반복
            sub = lst[i][j:j+N] # 이거 범위 제.대.로 
            if sub == sub[::-1]: # 첫번째 글자와 맨 끝 글자가 같으면 count 1씩 증가
                count +=1
    # 세로
    for j in range(8): # 이건 세로니까 j, i를 반대로 똑같이 하면 가로를 두번 하는 거겟지?
        for i in range(0, 8 - N + 1):
            sub = [] # 새로운 sub 빈 리스트 만들어주구 
            for q in range(N): # 회문의 길이 개수 만큼 지금 q만큼 반복해.
                sub.append(lst[ i + q ][j]) # 그 개수 만큼의 lst중에 있는 알파벳을 append 해
            sub= ''.join(sub) # sub에 넣어.
            if sub == sub[::-1]: # 그 sub에서 양끝글자가 같은게 있으면
                count += 1  # count 1씩 증가
    print(f"{test_case} {count}")