import sys
sys.stdin = open("input.txt","r")

"""
cost_pre = infinite  # 이전 비용

T = 시작온도

while T > T_end:          # T_end가 될 때까지 반복

    cost_new = cost( )      # 비용 계산

    diff = cost_new – cost_prev    # 새로운 비용과 이전 비용의 차이

    if difference < 0 or  e(-diff/T) > random(0,1):

        cost_pre = cost_new    # 비용이 감소하거나 확률이 랜덤 값보다 더 크면 비용 갱신

    T = T * k                 # k : cooling factor




다음과 같이 모의 담금질 기법을 구현하려고 한다.

cooling factor가 너무 작으면 T가 너무 급속하게 감소하고 너무 크면 연산량이 늘어나게 된다.

T와 T_end, k가 정해졌을 때 새로운 비용을 구하는 cost()의 반복 횟수를 계산하는 프로그램을 만드시오.


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 T, T_end, k가 주어진다.

1<=T<=10000,  0＜T_end＜= 1,  0.8 ＜= k ＜ 1

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.
 
"""
import math

T = int(input())

for i in range(T):
    T_start , T_end , k = input().split()

    t = int(T_start)
    end = float(T_end)
    kk = float(k)

    def cost_call(T_start, T_end, k):
        count = 0
        while T_start > T_end:
            T_start *= k
            count += 1

        return count
    
    print(f"#{i+1} {cost_call(t, end, kk)}")