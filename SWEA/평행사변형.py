# 정수 N이 주어질 때, 모든 변의 길이가 N인 가장 넓은 평행사변형의 넓이를 출력하라.
import sys
sys.stdin = open("sample_input.txt", "r")

def rectangle(N):
    res = N * N
    return res

T = int(input().strip()) # 테스트 개수

for test_case in range(1, T + 1):
    N = int(input())

    result = rectangle(N)

    print(f"#{test_case} {result}")