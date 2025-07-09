# <문제> 문제제목: 문제 설명
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

aa, b = '11', '25'
#a, b = map(int, input().split())
#print(a,b)
a_li = list(a)
b_li = list(b)
min, max = 0, 0

# min 구하기
for i in range(len(a)):
    if a_li[i] == '6':
        a_li[i] = '5'

    if b_li[i] == '6':
        b_li[i] = '5'

a_li = list(map(int, a_li))
b_li = list(map(int, b_li))

min = sum(a_li) + sum(b_li)  # ㅋㅋ머하냥 자리수가 다른딩 왜 다더해

a_li = list(a)
b_li = list(b)

# max 구하기
for i in range(len(a)):
    if a_li[i] == '5':
        a_li[i] = '6'

    if b_li[i] == '5':
        b_li[i] = '6'

a_li = list(map(int, a_li))
b_li = list(map(int, b_li))

max = sum(a_li) + sum(b_li)

print(min, max)