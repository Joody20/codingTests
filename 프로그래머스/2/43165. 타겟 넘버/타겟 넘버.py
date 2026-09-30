def solution(numbers, target):
    # 이게 지금 numbers에 있는 숫자로 target 숫자를 만들라는거잖아
    n = [0]
    
    for i in numbers:
        num = []
        for j in n:
            num.append(i+j)
            num.append(j-i)
        
        n = num
        
    return n.count(target)
        