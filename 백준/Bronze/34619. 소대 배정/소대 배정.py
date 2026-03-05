a,b,n,k = map(int,input().split())


# 1중대 1소대부터 채워지므로, k-1을 해준다.
k -= 1  
# 중대 번호 계산
company = k // (b * n) + 1
# 소대 번호 계산
platoon = (k % (b * n)) // n + 1
print(company, platoon)