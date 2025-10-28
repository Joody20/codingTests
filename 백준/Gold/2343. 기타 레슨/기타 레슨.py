N , M = map(int,input().split())
times = list(map(int,input().split()))


start = max(times) # 이  숫자보다 작은 크기는 존재하지 않음. [최소]
end = sum(times)      # 이 숫자보다 큰 크기는 존재하지 않음. [최대]

ans = 0

while start <= end:
    mid = (start + end) // 2        # 중간값
 
    total = 0        # 총 크기를 계산할 total
    count = 1        # 블루레이 개수를 셀 변수

    for t in times:
        if total + t > mid:      # 이번에도 넣으면 초과되는지 확인!
            count += 1           # 초과되면 블루레이 카운트를 늘려줘!!
            total = 0            # 새로운 블루레이를 시작해야 하니까 초기화를 해주고!!!!
        total += t               # 지금 강의를 새로운 블루레이에 첫 추가해준다..

    if count <= M:           # 블루레이 개수가 M의 개수보다 작거나 같으면
        ans = mid            # mid가 가능한 값일 때 마다 ans에 저장해주는거임.
        end = mid - 1        # end의 인덱스 위치를 mid의 위치에서 -1해준다.

    else:
        start = mid + 1      # start의 인덱스 위치를 mid + 1 해줌..

print(ans)


