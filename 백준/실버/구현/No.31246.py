import sys
sys.stdin = open("input.txt","r")

"""
모바일 광고 입찰

문제
모바일 광고 시장에서 광고 지면의 권리는 실시간 경매를 통해 결정된다. 이 경매에서는 각 지면에 대해 광고를 게재하고자 하는 회사들이 입찰가를 제시하며, 최고 입찰가를 제시한 회사가 해당 지면의 광고 권리를 얻는다. 이 과정은 전 세계 수많은 광고지면을 실시간으로 분석하고 입찰하는 기술적 도전을 포함한다.

MOLOCO는 고객사가 모바일 광고 시장에 접근할 수 있도록 도와주는 “MOLOCO 클라우드 DSP” 서비스를 운영한다. 이 서비스는 머신러닝을 기반으로 하여 초당 수백만 건 이상의 광고지면 입찰 요청을 처리한다. MOLOCO는 고객사들을 대신하여 입찰에 참여하며, 고객사가 최적의 가격으로 광고지면을 구매할 수 있도록 지원한다.

당신은 MOLOCO에서 클라우드 DSP 서비스를 개선하는 일을 맡고 있으며, 당신의 목표는 과거 중요한 광고지면 
$N$개에 대한 입찰 데이터를 분석하여, 입찰 가격 결정 로직을 개선하는 것이다.

각 광고지면 i에 대해 MOLOCO가 제시한 입찰 가격 A_i와 MOLOCO의 입찰가를 제외한 다른 모든 입찰가 중 최고 가격 
B_i가 주어진다. 당신은 MOLOCO가 모든 입찰가를 일괄적으로 X만큼 올렸을 때, (즉, MOLOCO의 입찰가를 A_i에서 A_i로 일괄적으로 올리는 것이다.) 
K개 이상의 지면을 낙찰받게 되는 가장 작은 음이 아닌 정수 X를 찾고자 한다. 단, 같은 지면에 대해 MOLOCO의 입찰가와 다른 회사의 최고 입찰가가 같을 경우 MOLOCO가 낙찰받는다고 가정한다.

입력
첫 번째 줄에는 전체 분석 대상 광고 지면의 수 
$N$과 목표 낙찰 지면 수 
$K$가 공백으로 구분되어 주어진다.

다음 
$N$개의 줄에 광고지면 
$i$에 대한 정보 
$A_i$와 
$B_i$가 공백으로 구분되어 차례로 주어진다.

출력
MOLOCO의 입찰가를 일괄적으로 
$X$만큼 올렸을 때, 최소 
$K$개 이상의 지면을 낙찰받는 음이 아닌 최소 정수 
$X$를 출력하라.


예제 1
3 2
3 1
2 1
1 2

출력 1
0
-> 이미 MOLOCO가 2개의 지면을 낙찰받았기 때문에, 입찰 가격을 변경할 필요가 없어 답은 0이다.

예제 2
3 2
10 30
21 19
10 12

출력 2
2

"""
import heapq

N , K = map(int,input().split())
advers = [list(map(int,input().split())) for _ in range(N)]

cnt = 0  # K랑 비교하기 위한 카운트 수
min_prices = []

for A,B in advers:
    if A >= B:  # MOLOCO거가 더 큰 경우
        cnt += 1
    else:
        min_price = B - A
        if min_price > 0:
            heapq.heappush(min_prices, min_price)
        else:
            continue

if cnt == K:  # cnt와 K가 같으면 X를 리턴하는데 잠만,
    print(0)

elif cnt + len(min_prices) < K:
    print(-1)

else: # cnt가 K보다 작으면 이제 입찰을 올려야돼. 근데 최소가격을 올려야 하니까?
    need = K - cnt  # 몇개의 입찰 가격을 올려야 하는지를 안해줬어... 이거 해주고
    result = 0

    for _ in range(need):
        result += heapq.heappop(min_prices)

    print(result)




