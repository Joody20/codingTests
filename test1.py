# with open("input.txt", "r") as file:
#     lines = file.readlines()


# n=0
# # Process each test case
# for index,line in enumerate(lines):
#     if (index+1) % 2 == 0:
#         line_sum = 0
#         numbers = [int(num.strip()) for num in line.split('+') if num.strip().isdigit()]
#         line_sum += sum(numbers)
#         n+=1
#         print(f"#{n} {line_sum}")



# import sys
# sys.stdin = open("input.txt", "r")

# T = int(input().strip())

# n=0
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     lines = sys.stdin.readlines()
#     for index,line in enumerate(lines):
#         if (index+1) % 2 == 1:
#             line_sum = 0
#             numbers = [int(num.strip()) for num in line.split('+') if num.strip().isdigit()]
#             line_sum += sum(numbers)
#             n+=1
#             print(f"#{n} {line_sum}")
        

# # 이건 이제 표준입출력만으로 하는
# for test_case in range(1, T + 1):
#     N = int(input().strip())
#     str = input().strip()
    
#     answer = 0  # Initialize the answer
#     for char in str:
#         if char != '+':  # Ignore '+' characters
#             answer += int(char)  # Sum the integer values of the characters
    
#     # Print the result in the required format

#     print(N)
#     print(answer)
#     print(f"#{test_case} {answer}")




# 준환이의 운동관리

#최근 경도비만 판정을 받은 준환이는 적절한 몸을 유지하기 위하여 1주일에 L분 이상 U분 이하의 운동을 하여야 한다.

#준환이는 이번 주에 X분만큼 운동을 하였다.

#당신은 준환이가 제한되어 있는 시간을 넘은 운동을 한 것인지, 그것이 아니라면 몇 분 더 운동을 해야 제한을 맞출 수 있는지 출력하는 프로그램을 작성해야 한다.

# b, c = map(int, input().split())

"""
import sys
sys.stdin = open("sample_input.txt", "r")

def exercise(L,U,X):
    if(X < L):
        I = L - X
        return I
    elif (L <= X <= U):
        return 0
    
    elif(X > U):
        return -1
    
T = int(input().strip()) # 테스트 개수

for test_case in range(1, T + 1):
    L, U, X = map(int, input().split())  # 공백으로 구분된 세 개의 정수를 입력받습니다.

    result = exercise(L,U,X)

    print(f"#{test_case} {result}")

"""    


#조별과제
 #당신은 교수이다. 매주 월요일과 수요일 오전 9시부터 10시 30분까지 진행되는 당신의 수업에는 N명의 수강생이 있다. 당신은 학생들에게 조별과제를 부여하기 위해 학생들을 몇 개의 조로 나누려고 한다.

  #당신은 한 조가 2명 이하의 학생으로 구성되면 토론이나 업무 배분 등이 제대로 이루어지지 않아 팀워크를 평가할 기회를 박탈당한다고 생각한다. 따라서, 당신은 3명 이상의 학생으로 구성된 조의 수를 최대화하려고 한다. 각 학생은 정확히 한 개의 조에만 속할 수 있다.

  #학생들을 조로 적당히 나누었을 때, 3명 이상의 학생으로 구성된 조의 수의 최댓값이 얼마인지를 구하는 프로그램을 작성하라.

#[입력]
  #첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
  #각 테스트 케이스는 하나의 줄로 이루어진다. 각 줄에는 학생의 수 N (1 ≤ N ≤ 1000)이 주어진다.

#[출력]
  #각 테스트 케이스마다, N명의 학생들을 조로 적당히 나누었을 때, 3명 이상의 학생으로 구성된 조의 수의 최댓값을 출력한다.

"""
import sys
sys.stdin = open("sample_input.txt", "r")

def Max_student(N):
    if(N >= 3):
        max_num = N // 3
        return max_num
    else:
        return 0

T = int(input().strip()) # 테스트 개수

for test_case in range(1, T + 1):
    N = int(input())
    result = Max_student(N)

    print(f"#{test_case} {result}")

"""


# 평행사변형
# 정수 N이 주어질 때, 모든 변의 길이가 N인 가장 넓은 평행사변형의 넓이를 출력하라.

"""
import sys
sys.stdin = open("sample_input.txt", "r")

def rectangle(N):
    res = N * N
    return res

T = int(input().strip()) # 테스트 개수

for test_case in range(1, T + 1):
    N = int(input())

    result = rectangle(N)

    print(f"#{test_case} {result}")
"""



#구구단 2
# 아기 석환이는 최근 구구단을 배웠다. 그래서 1 이상 9 이하의 자연수 두개를 곱셈할 수 있으나, 10 이상의 자연수를 곱셈하는 방법은 모른다.
#두 정수 A, B가 주어진다. 아기 석환이 두 정수를 곱셈할 수 있으면 곱을 출력하고, 아니면 -1을 출력하라.

"""
import sys
sys.stdin = open("sample_input.txt", "r")

def gugudan(A,B):
    if(1<=A<=9 and 1<= B <= 9):
        mul = A * B
        return mul
    elif(1<=B<=9 and 10<=A<=20):
        return -1
    elif(1<=A<=9 and 10<=B<=20):
        return -1
    elif (10<=A<=20 and 10<=B<=20):
        return -1

T = int(input().strip()) # 테스트 개수

for test_case in range(1, T + 1):
    A,B = map(int, input().split())

    res = gugudan(A,B)

    print(f"{test_case} {res}")
"""


# 소득 불균형

# 예를 들어, 대다수의 국가에서는 적은 수의 사람이 국가 전체 소득의 꽤 많은 부분을 차지하기 때문에, 해당 국가의 평균 소득은 보통 사람들의 소득보다 높은 경우가 많다.

# 당신은, n명의 사람의 소득이 주어졌을 때 이 중 평균 이하의 소득을 가진 사람들의 수를 출력해야 한다.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 이후 T개의 테스트 케이스에 대해 각각 두 줄로 주어진다.

# 첫 번째 줄에는 정수의 개수 N 이 주어지며(1 ≤ N ≤ 10,000), 두 번째 줄에는 각 사람의 소득을 뜻하는 N개의 양의 정수가 주어진다. 이 정수들은 각각 1 이상 100,000 이하이다.
 

# [출력]

# 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,

# 각 테스트 케이스마다 한 줄씩 평균 이하의 소득을 가진 사람들의 수를 출력한다.

"""
import sys
sys.stdin = open("sample_input.txt", "r")

def multiple(N,W):
    res = len([x for x in W if x <= sum(W)/N])
    return res

T = int(input().strip()) # 테스트 개수

for test_case in range(1, T + 1):
    N= int(input())
    W= list(map(int,input().split()))


    result = multiple(N,W)

    print(f"{test_case} {result}")
"""

#in-order Tree 구현하기

"""
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

"""

