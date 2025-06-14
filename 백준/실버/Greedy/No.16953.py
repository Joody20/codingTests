import sys
sys.stdin = open("input.txt","r")


# 문제
# 정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

# 2를 곱한다.
# 1을 수의 가장 오른쪽에 추가한다. 
# A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

# 입력
# 첫째 줄에 A, B (1 ≤ A < B ≤ 109)가 주어진다.

# 출력
# A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 만들 수 없는 경우에는 -1을 출력한다.


A,B = map(int, input().split())

# A가 B가 되어야 하는데 
count = 0  # 연산횟수

while A < B:

    # 이게 맨오른쪽에 1을 붙여주는 조건
    if B % 10 == 1:
        B = (B - 1) // 10

    # 짝수일 때의 조건
    elif B % 2 == 0:
        B //= 2

    else:
        break
    
    # count 세줌.
    count += 1

# A == B이면 count에 1 더해주고
if A == B:
    print(count+1)
else:
    print(-1)



