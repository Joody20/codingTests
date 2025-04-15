import sys
sys.stdin = open("input.txt","r")


def num(n,m):
    if m == 1:
        return n
    
    return n * num(n,m-1)


for _ in range(10):
    t = int(input())
    n,m = map(int,input().split())

    print(f"#{t} {num(n,m)}")