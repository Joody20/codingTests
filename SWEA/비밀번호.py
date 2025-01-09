for test_case in range(1, 11):
    N,string = input().split()

    ans = []
    for i in string: # 문자열이니까 그냥 range() 안쓰고 string 으로 해줬으면 됐지 개멍청한 새끼야
        if not ans or ans[-1] != i:  # ans가 없거나 ans의 끝문자와 지금 현재 i의 문자가 같지 않으면 넣어
            ans.append(i)
        else: # 만약 같다면? 빼
            ans.pop()

    
    result = "".join(ans) # ans를 "" 빈 문자열에 넣어서 
    print(f"#{test_case} {result}")