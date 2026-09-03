def solution(a, b, n):
    coke = 0
    
    # 일단 계산식은 빈병 n - 최대 빈병을 얻을 수 있는 a의 배수 + 얻은 빈병의 개수
    # -> 이걸 계속 반복하는거야.
    while n >= a:
        exchange = (n // a) * b
        coke += exchange
        n = (n % a) + exchange
    
    return coke