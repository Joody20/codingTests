import sys
sys.stdin = open("input2.txt", "r")

def inOrder(n):
  if n <= N: # 데이터 개수보다 작아질 경우까지만 
    inOrder(n*2) #왼쪽노드
    ans.append(node_list[n])  #현재 노드 인덱스에 있는 문자를 더해
    inOrder(n*2+1) # 그 다음 이제 오른쪽 노르
  
T = 10  # 테스트 개수
for test_case in range(1, T + 1):
  N = int(input()) # 데이터 가져오지요
  node_list = [0] * (N+1) # 각 노드의 문자를 저장할 리스트야 이게
  for i in range(1,N+1):
    node_list2 = input().split() # 공백으로 문자를 구분하고
    node_list[i] = node_list2[1] # 첫번째거부터 이제 node_list에 넣어

  ans  = [] # 결과를 저장할 빈 리스트 선언
  inOrder(1) # 루트노드부터 시작하니까 항상 1로 시작
  print(f'#{test_case} {"".join(ans)}')