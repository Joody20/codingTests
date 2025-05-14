import sys
sys.stdin = open("input.txt")
"""
2이상인 정수 중 1과 자기 자신만으로 나누어 지는 수를 소수라 한다.

두 개의 정수 a, b가 주어지면 a ＜ p ＜ b 를 만족하는 모든 소수 p의 합을 구하는 프로그램을 만드시오.

[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 두 개의 정수 a, b가 공백을 두고 주어진다.

1<=a,b<=1,000,000
 
[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.

예제 1
3
1 10
5 20
100 1000

출력 1

#1 17
#2 67
#3 75067

"""
#  소수 구하는 함수!
def division(n):  
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        
    return True

T = int(input())

for i in range(T):
    a,b = map(int,input().split())
    p = 0
    summ = 0

    for p in range(a+1,b):
        if division(p):
           summ += p
    print(f"#{i+1} {summ}")
