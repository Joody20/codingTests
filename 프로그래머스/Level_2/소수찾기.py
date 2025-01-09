from itertools import permutations
def solution(numbers):
    nums = list(numbers) # 입력된 문자열을 리스트로 변환
    count = 0  # 횟수 세는거 
    valid  = set() # 가능한 조합들 (중복 제거)
    
    for i in range(len(numbers)):
        valid |= set(map(int, map("".join, permutations(nums, i+1))))
        # permutations(nums, i+1): i+1 길이의 모든 순열 생성
        # "".join : 생성된 순열을 문자열로 합침.
        # map(int, ---) : --- 을 int형으로 바꿈....
        # set(~~) : 중복 제거를 위해 집합으로 바꿈.
        # |=: 기존 valid 집합에 새로운 값을 추가 (합집합)

    valid -= set(range(0,2)) # 0과 1은 소수가 아니므로 제거
    
    for i in valid: # 가능한 집합에서
        # i가 소수인지 확인
        # range(2, int(i**0.5)+1) 범위의 숫자 중 i로 나누어 떨어지는 수가 없으면 소수
        if not sum(1 for j in range(2, int(i**0.5)+1) if i%j == 0) : count += 1
        # 소수라면 count 1씩 증가
        
    return count