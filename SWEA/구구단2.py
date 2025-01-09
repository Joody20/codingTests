# 아기 석환이는 최근 구구단을 배웠다. 그래서 1 이상 9 이하의 자연수 두개를 곱셈할 수 있으나, 10 이상의 자연수를 곱셈하는 방법은 모른다.
#두 정수 A, B가 주어진다. 아기 석환이 두 정수를 곱셈할 수 있으면 곱을 출력하고, 아니면 -1을 출력하라.
import sys
sys.stdin = open("sample_input.txt", "r")

def gugudan(A,B):
    if(1<=A<=9 and 1<= B <= 9):
        mul = A * B
        return mul
    elif(1<=B<=9 and 10<=A<=20):
        return -1
    elif(1<=A<=9 and 10<=B<=20):
        return -1
    elif (10<=A<=20 and 10<=B<=20):
        return -1

T = int(input().strip()) # 테스트 개수

for test_case in range(1, T + 1):
    A,B = map(int, input().split())

    res = gugudan(A,B)

    print(f"{test_case} {res}")