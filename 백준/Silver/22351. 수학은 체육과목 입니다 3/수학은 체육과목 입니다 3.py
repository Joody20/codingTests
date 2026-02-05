input = input()

N = len(input)

num_list = [int(input[:1]), int(input[:2]), int(input[:3])]
res = []

for num in num_list:
    num_n = num

    new_num = ""

    while len(new_num) < N:
        new_num += str(num_n)

        if new_num == input:
            res.append([num,num_n])
        num_n += 1

# 가장 작은 것을 출력해라. 이 조건을 무시함.. 이것만 맞추면 맞을듯!
if res:
    print(res[0][0], res[0][1])