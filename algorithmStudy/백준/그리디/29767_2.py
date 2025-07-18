# 백준 29767번
# <문제> 점수를 최대로: 문제 설명
"""
단대소프트고에는 교실 
$N$개가 있다. 교실은 
$1$번부터 
$N$번까지 
$1, 2, \ldots, N$ 순서로 연달아 있다.

학교 밖에는 
$K$명의 학생들이 있다. 
$K$명의 학생은 학교에 들어가기 전 학생마다 목적지 교실을 정하게 된다. 
$j$번째 학생의 목적지는 
$B_j$번 교실이다. 학생들의 목적지는 모두 달라야 한다. 
$j$번째 학생은 
$1$번 교실, 
$2$번 교실, 
$\ldots, B_j$번 교실까지 모든 교실에 들어갔다 나오게 된다. 마지막 교실까지 들어갔다 나오게 되면 아무 교실도 방문하지 않고 다시 학교 밖으로 나간다.

모든 학생의 방문이 끝나면, 교실의 점수를 구할 수 있다. 
$i$번째 교실의 점수는 
$A_i$ × (
$i$번째 교실에 학생이 들어갔다 나온 횟수)가 된다. 학생들은 학교에 들어가기 전 방문 후의 교실의 점수의 합이 최대가 되도록 의논하여 목적지를 정한다. 이때 방문이 끝난 후 모든 교실의 점수의 합을 구해보자.
"""

# 입력
"""
첫째 줄에 
$N$과 
$K$가 공백으로 구분되어 입력된다. 
$(1≤K≤N≤300\,000)$ 

둘째 줄에 정수 
$A_1, A_2, ... A_N$이 공백으로 구분되어 입력된다. 
$(-10^8≤A_i≤10^8)$ 

5 3
3 -5 2 -1 4
"""

# 출력
"""
첫째 줄에 방문이 끝난 후 모든 교실의 점수의 합을 출력한다.

6

학생들의 목적지를 1번, 3번, 5번 교실로 정한다.

1번 교실의 방문 횟수는 3이고 교실의 점수는 3 × 3 = 9가 된다.
2번 교실의 방문 횟수는 2이고 교실의 점수는 -5 × 2 = -10가 된다.
3번 교실의 점수는 2 × 2 = 4이다.
4번 교실의 점수는 -1 × 1 = -1이다.
5번 교실의 점수는 4 × 1 = 4다.
모든 교실의 점수의 합은 9 - 10 + 4 - 1 + 4 = 6이고 이 경우가 최대가 된다.
"""

# 내 풀이 아이디어
"""

"""
# 입력부
# n,k = map(int, input().split())    # 교실n 학생k
# score = map(int, input().split())  # 교실별 점수
# list_score = [*score] # 각 후보별 득표수를 담을 리스트
import heapq

n, k = 5, 3
list_score = [3,-5,2,-1,4]

# 교실1에 3번 -> 3*3=9
# 교실2에 2번 -> -5*2=-10
# 교실3에 1번 -> 2*1=2

# 총합은 9-10+2 = 1

# 학생1이 교실1까지갔을 때, 3
# 학생2이 교실2까지갔을 때, 3-5 = -2
# 학생3이 교실3까지갔을 때, 3-5+3 = 0

# 총합은 3-2+0 = 1

# 위 두 개의 case가 같다고 볼 수 있다.

# list_score[0]*1 + list_score[1]*1 + ... + list_score[-1]*1
# 리스트 이름 뭘로하지.... 이게 제일 어렵다 진짜루....
# individual_list..?
sum=0
individual_list = []

for i in list_score:
    sum +=i
    individual_list.append(sum)


def heapsort(iterable):
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)  # 맥스힙만드려면 -value
    print(h)
    
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))  # 여기도 맥스힙만들때 부호복원
    
    print(result)
    return result

res = heapsort(individual_list)

res_val = 0


for i in range(k):
    res_val += res[i]
    #print("res_val",res_val)
    
print(res_val)




# Discussion
"""
자료구조 힙을 처음 써서 풀어본 코테문제이다..
와 이거 재밌다. 이게 '앎'의 기쁨.
깨달았다.. 자료구조 영상 코드 다 구현하고 다 뜯어봐야한다..
다시 자료구조 들어야겠다..
"""