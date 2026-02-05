num = int(input()) + 1
str_num = str(num)


first = int(str_num[:2])
second = int(str_num[2:])


while num != (first + second) ** 2:
    num += 1
    str_num = str(num)
    first = int(str_num[:2])
    second = int(str_num[2:])
    
if num > 9999:
    print(-1)
else:
    print(num)


