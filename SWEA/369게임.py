T = int(input())

for tc in range(1, T + 1):
    num = str(tc)

    ans = []

    num = num.replace('3','-')
    num = num.replace('6','-')
    num = num.replace('9','-')

    if len(num) == 2 and num.count('-') == 1:
        num = num.replace(num, '-')

    ans.append(num)

    for item in ans:
        print(item, end= ' ')