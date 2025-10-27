N = int(input())

lost_power = list(map(int,input().split()))
gain_happy = list(map(int,input().split()))


power = 100

dp = [0] * (power+1)
dp[power] = 0  # 처음 체력일 때 기쁨도 0

for i in range(N):
    ph = lost_power[i]
    gh = gain_happy[i]

    for j in range(power, ph-1, -1):
        # 체력이 음수이면 기쁨 사라지기 때문에 체력이 양수일 때만 계산
        if j - ph > 0: # j - ph = power이야 지금!! 그래서 이 power이 양수일 때만 dp업데이트해줘서 max값 찾기
            dp[j] = max(dp[j], dp[j - ph] + gh)


print(dp[power]) # 최대 기쁨도