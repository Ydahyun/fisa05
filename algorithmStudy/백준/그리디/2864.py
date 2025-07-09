# 백준 2864번
# <문제> 5와 6의차이: 문제 설명
"""
상근이는 2863번에서 표를 너무 열심히 돌린 나머지 5와 6을 헷갈리기 시작했다.

상근이가 숫자 5를 볼 때, 5로 볼 때도 있지만, 6으로 잘못 볼 수도 있고, 
6을 볼 때는, 6으로 볼 때도 있지만, 5로 잘못 볼 수도 있다.

두 수 A와 B가 주어졌을 때, 상근이는 이 두 수를 더하려고 한다. 
이때, 상근이가 구할 수 있는 두 수의 가능한 합 중, 
최솟값과 최댓값을 구해 출력하는 프로그램을 작성하시오.
"""

# 입력
"""
첫째 줄에 두 정수 A와 B가 주어진다. (1 <= A,B <= 1,000,000)
11 25
"""

# 출력
"""
첫째 줄에 상근이가 구할 수 있는 두 수의 합 중 최솟값과 최댓값을 출력한다.
36 37
"""

# 내 풀이 아이디어
"""
이거그냥 문자열 순회돌고 최솟값할땐 6을 5로 바꾸고,
최대값할땐 5를 6으로 바꿔서 더하면되는거아인교...?


"""

a, b = map(str, input().split())  # str로 받는 이유는 아래에..

min, max = 0, 0

#### 값 대체를 어떻게 할 지 고민을 많이했숨당
#### 숫자는 값을 못바꿔주니까 리스트에 넣었어용

a_li_min = list(a)
b_li_min = list(b)
a_li_max = list(a)
b_li_max = list(b)


 
# a처리기
for i in range(len(a)):
    if a_li_min[i] == '6':
        a_li_min[i] = '5'

    if a_li_max[i] == '5':
        a_li_max[i] = '6'

# b처리기
for i in range(len(b)):
    if b_li_min[i] == '6':
        b_li_min[i] = '5'

    if b_li_max[i] == '5':
        b_li_max[i] = '6'

# 각 리스트들 int로 형 변환 해서 다시 대입해주궁
a_li_min = list(map(int, a_li_min))
a_li_max = list(map(int, a_li_max))
b_li_min = list(map(int, b_li_min))
b_li_max = list(map(int, b_li_max))

# 자리 수에 맞게 *(10^n)을 해줘서 단위를 맞춰주기~

# a_li_min = [1, 1]   -(변환)--> [10, 1]

for i in range(0,len(a_li_min)):
    a_li_min[i] = a_li_min[i]* ( 10**(len(a_li_min)-i-1) )

for i in range(0,len(a_li_max)):
    a_li_max[i] = a_li_max[i]* ( 10**(len(a_li_max)-i-1) )
    
for i in range(0,len(b_li_min)):
    b_li_min[i] = b_li_min[i]* ( 10**(len(b_li_min)-i-1) )

for i in range(0,len(b_li_max)):
    b_li_max[i] = b_li_max[i]* ( 10**(len(b_li_max)-i-1) )

min = sum(a_li_min) + sum(b_li_min)
max = sum(a_li_max) + sum(b_li_max)

print(min, max)

# Discussion
"""
1. 변수 명으로 사용했던
min, max는 파이썬 내장함수와 이름을 겹치니
min_val, max_val과 같이 고쳐주는게 좋음.

2. 문자열 치환을 이용하면 더 간단하게 풀 수 있다.

a, b = input().split()

# 최소값: 6을 5로 모두 바꿔서 합
min_val = int(a.replace('6', '5')) + int(b.replace('6', '5'))
# 최대값: 5를 6으로 모두 바꿔서 합
max_val = int(a.replace('5', '6')) + int(b.replace('5', '6'))

print(min_val, max_val)


"""