T = int(input())

def cal(n):
    if n == 1:
        return 1
    elif( n % 2 == 1):
        return n + cal(n-1)
    elif(n%2 == 0):
        return -n + cal(n-1)
    
for test_case in range(1, T + 1):
    N = int(input().strip())

    result = cal(N)

    print(f"#{test_case} {result}")