# 백준 2798번
# <문제> 블랙잭: 문제 설명
"""

"""

# 입력
"""

"""

# 출력
"""

"""

# 내 풀이 아이디어
"""
조합 nC3써서 sum해서 제일 가까운거 출력하자
브루트포스 
"""


from itertools import combinations

N, M = map(int, input().split())
card_list = list(map(int, input().split()))  # int형으로 담으려면 list()해줘야함.
# print(card_list)  # ['5', '6', '7', '8', '9'] 리스트에 담김
# print(card_list)    # [5, 6, 7, 8, 9]


combi = list(combinations(card_list, 3))
#print(combi) 
# [(5, 6, 7), (5, 6, 8), (5, 6, 9), (5, 7, 8), (5, 7, 9), (5, 8, 9), (6, 7, 8), (6, 7, 9), (6, 8, 9), (7, 8, 9)]
combi_sum = []
for i in combi:
    if sum(i)<M:
        combi_sum.append(sum(i))
print("combi_sum\n",combi_sum)
#[18, 19, 20, 20, 21, 22, 21, 22, 23, 24]
diff = []
for i in combi_sum:
    diff.append(abs(i-M))
print("diff\n", diff)
# [3, 2, 1, 1, 0, 1, 0, 1, 2, 3]
print(diff.index(min(diff)))  # 4
if len(diff) == 0:
    print(M)
else:
    print(combi_sum[diff.index(min(diff))])


# Discussion
"""

"""