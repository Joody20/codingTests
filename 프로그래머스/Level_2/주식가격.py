def solution(prices):
    # 현재 prices의 가격이 뒤에 있는 prices보다 가격이 같거나 크면 그 길이만큼 초를 더함.
    # 현재 prices의 가격이 뒤에 있는 prices보다 가격이 작으면 +1초만함.
    # 맨 뒤에 prices는 그냥 0을 리턴함.
    
    res = [0] * len(prices) # 여기에 이제 가격이 떨어지지 않은 기간이 몇초인지를 넣을거야
    
    for i , price in enumerate(prices):
        for j in range(i+1, len(prices)):
            if price <= prices[j]:
                res[i] += 1
            else: # 지금 가격이 다음 가격보다 큰 경우 잖아 그니까 값이 떨어지는 경우
                res[i] = j - i
                break
    return res
    

    