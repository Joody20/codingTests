import math
def solution(arr):
    while len(arr) >= 2:
        a,b = arr[0], arr[1] # 2, 6 -> 6
        arr.append((a*b) // math.gcd(a,b)) # 8 14 6
        arr = arr[2:] # 2 6 8 14 -> 이미 앞에 두개 꺼는 계산을 했으니까... 2 6 빼고 그 다음은 또 8, 14 빼고 8 , 14 계산한게 뒤에 붙으니까 
        # 6 56 계산하고 그러면 하나 남으니까 ㄹㅈㄷ ㄹㅈㄷ ㄹㅈㄷ..... 2개씩 계속 계산해나간거지 저 최소 공배수 구하는 식이 2개의 숫자를 가지고 하는 공식이다보니까...
    return arr[0]