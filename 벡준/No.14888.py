T = int(input())

# T개의 숫자를 입력받음
numbers = list(map(int, input().strip().split()))

# 각 연산자의 개수를 입력 받음.
operate = list(map(int, input().strip().split()))

def solution(idx, current_result, add, sub, mul, div):
    global max_value , min_value

    if idx == T:  # idx가 T와 같아지면 이제 현재값에서 max와 min값을 추출함.
        max_value = max(max_value, current_result)
        min_value = min(min_value, current_result)
        return
    
    #각 연산자를 하나씩 사용하면서 다음 숫자로 계산
    if add > 0 :  # 트러블 슈팅 ! -> elif로 하니까 값이 안나오고 if문으로 해야 제대로된 값이 나왓음.
        solution(idx + 1 , current_result + numbers[idx] , add - 1 , sub , mul , div )  # add - 1 이렇게 하는 이유는 한번 계산 했으면 빼야돼서
    if sub > 0:
        solution(idx + 1 , current_result - numbers[idx] , add , sub - 1 , mul , div )
    if mul > 0:
        solution(idx + 1 , current_result * numbers[idx] , add , sub , mul - 1 , div )
    if div > 0:
        if numbers[idx] != 0: # 나눗셈을 0으로 계산하지 않게끔
            solution(idx + 1 , int(current_result / numbers[idx]) , add , sub , mul , div - 1 )

# 최대값과 최소값 초기화
max_value = -float("inf")
min_value = float("inf")

# 함수에 각 숫자 넣어주기
solution(1, numbers[0] , operate[0] , operate[1] , operate[2] , operate[3])

print(max_value)
print(min_value)