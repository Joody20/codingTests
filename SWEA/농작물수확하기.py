T = int(input().strip())  # 테스트의 개수

for test_case in range(1,T+1):
    N = int(input()) # 데이터 input
    lst = []  # 빈 리스트 생성
    for _ in range(N):
        tmp = list(map(int,input()))   # 숫자들을 map으로 받아서 list로 가져오고
        lst.append(tmp) # 이걸 list에 append해

    farm = int((N-1)/2)  # 마름모 모양을 만들기 위해 중앙 인덱스를 계산
    value = sum(lst[farm]) # 마름모 내부에 있는 가운데 줄의 값들을 더함

    i=0
    while i < farm: # farm이 0이 아닐때까지 무한반복
        value += sum(lst[i][farm-i:farm+i+1]) # 위쪽 마름모 부분의 값들을 더함 
        value += sum(lst[N-i-1][farm-i:farm+i+1])# 아래쪽 마름모 부분의 값들을 더함

        i+=1
    print(f"#{test_case} {value}")