import sys
sys.stdin = open("input.txt","r")
"""
정해진 횟수만큼 교환이 끝나면 숫자판의 위치에 부여된 가중치에 의해 상금이 계산된다.

숫자판의 오른쪽 끝에서부터 1원이고 왼쪽으로 한자리씩 갈수록 10의 배수만큼 커진다.

위의 예에서와 같이 최종적으로 숫자판들이 8,8,8,3,2의 순서가 되면 88832원의 보너스 상금을 획득한다.

여기서 주의할 것은 반드시 횟수만큼 교환이 이루어져야 하고 동일한 위치의 교환이 중복되어도 된다.

다음과 같은 경우 1회의 교환 횟수가 주어졌을 때 반드시 1회 교환을 수행하므로 결과값은 49가 된다.

94의 경우 2회 교환하게 되면 원래의 94가 된다.

정해진 횟수만큼 숫자판을 교환했을 때 받을 수 있는 가장 큰 금액을 계산해보자.

[입력]

가장 첫 줄은 전체 테스트 케이스의 수이다.

최대 10개의 테스트 케이스가 표준 입력을 통하여 주어진다.

각 테스트 케이스에는 숫자판의 정보와 교환 횟수가 주어진다.

숫자판의 정보는 정수형 숫자로 주어지고 최대 자릿수는 6자리이며, 최대 교환 횟수는 10번이다.

[출력]

각 테스트 케이스마다, 첫 줄에는 “#C”를 출력해야 하는데 C는 케이스 번호이다.

같은 줄에 빈 칸을 하나 사이에 두고 교환 후 받을 수 있는 가장 큰 금액을 출력한다.

예제 1
10
123 1
2737 1
757148 1
78466 2
32888 2
777770 5
436659 2
431159 7
112233 3
456789 10

출력 1
#1 321
#2 7732
#3 857147
#4 87664
#5 88832
#6 777770
#7 966354
#8 954311
#9 332211
#10 987645

"""
#방법 2
def dfs(n):
    global answer   # 최종값을 리턴할건데.
    if n == cnt:  # n이 교환횟수와 같아지면,
        answer = max(answer, int("".join(map(str,arr))))  # answer을 max값으로 리턴
        return
    
    for i in range(k):
        for j in range(i+1, k):
            arr[i] , arr[j] = arr[j], arr[i]   # 두 개의 값을 바꿔줄거야
            num = int("".join(map(str,arr)))  # 이 때의 nums을 가지고 있어

            if (n,num) not in visited: # 이게 visited에 없다면
                dfs(n+1)  # 교환횟수 1증가
                visited.append((n,num))  # visited에 넣어주고
            arr[i], arr[j] = arr[j], arr[i]  # 백트래킹 시도


T = int(input())

for t in range(T):
    a,b = input().split()
    cnt = int(b)  # 교환횟수 int형으로 줫어야지..

    arr = list(map(int,a))
    k = len(arr)

    answer = -1
    visited = []
    dfs(0)
    print(f"#{t+1} {answer}")


"""
방법 1
T = int(input())
for t in range(T):
    nums , change = input().split()

    arr = list(map(int,nums))
    k = int(change)
    stack = [(arr[:], 0)]  # 현재 배열과, 교환횟수를 넣어주는거야

    visited = set()  # 그 숫자를 방문했는지를 체크하기 위함임.
    max_result = int("".join(map(str,arr)))  # max_value를 찾기 위해

    while stack:
        cur_arr , cnt = stack.pop()
        cur_key = (tuple(cur_arr), cnt)

        if cur_key in visited:
            continue
        visited.add(cur_key)

        if cnt == k:
            max_result = max(max_result , int("".join(map(str,cur_arr))))
            continue
        
        n = len(cur_arr)
        for i in range(n):
            for j in range(i+1 , n):
                cur_arr[i], cur_arr[j] = cur_arr[j], cur_arr[i]
                stack.append((cur_arr[:], cnt + 1))
                cur_arr[i], cur_arr[j] = cur_arr[j], cur_arr[i]

    print(f"#{t+1} {max_result}")


"""
    
