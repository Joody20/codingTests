T = int(input())

for i in range(1, T + 1):
    N = int(input())

    number = [2,3,5,7,11] # 배열은 항상 인덱스를 가지고 있으니까 인덱스에 대한 값을 가지고 올때는 이런 배열 형태로 해주는게 ***

    ans = []

    for j in range(len(number)):   # number 안에 있는 숫자 만큼 반복
        while (N % number[j] == 0):  # N이 number[j]의 숫자로 나눴을 때 나머지가 0이 될때까지 반복
            ans.append(number[j]) # number[j]의 숫자를 ans 안에 넣어..... 아 ㄹㅈㄷ
            N = N // number[j]  # # number[j] 를 계속 나눠 몫만 남게

    a = ans.count(2) # 숫자 2가 있는 만큼 count
    b = ans.count(3) # 숫자 3이 몇개 있는지 count 함수 쓴거임
    c = ans.count(5)
    d = ans.count(7)
    e = ans.count(11)


    print(f"#{i} {a} {b} {c} {d} {e}")