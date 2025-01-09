T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    correct_string = list(input().strip())
    writing_string = list(input().strip())

    count = 0

    for i in range(0, N):
        if(correct_string[i] == writing_string[i]):
            count += 1

    print(f"#{test_case} {count}")