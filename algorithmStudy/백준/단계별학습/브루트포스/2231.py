# 백준 2231번
# <문제> 분해합: 문제 설명
"""
245+2+4+5
245+11=256

198+1+9+8
198+18=216

216

1+2+3+123
6+123=129
"""

# 입력
"""

"""

# 출력
"""

"""

# 내 풀이 아이디어
"""

"""
from itertools import product
from itertools import combinations
N=216
M=0
num_list_int = [1,2,3,4,5,6,7,8,9,0]
num_list_str = ['1','2','3','4','5','6','7','8','9','0']
prods = list(product(num_list_str, repeat=3))
prods_int = list(product(num_list_str, repeat=3))
combis = list(combinations(num_list_int, 3))
#print("prod",prods)
#print("prods_int",prods_int)
#print("combi", combis)
prod_to_num = []  # int형으로 가능한 숫자 담을 리스트

for i in range(len(prods)):
    prod_to_num.append((prods[i][0]+prods[i][1]+prods[i][2]))
#print("prod_to_num", prod_to_num)

combis_sum = []
for i in combis:
    combis_sum.append(sum(i))
#print("combis_sum", combis_sum)
can_ = []
for i in range(len(prods_int)):
    can_.append(int(prod_to_num[i])+int(prods_int[i][0])+int(prods_int[i][1])+int(prods_int[i][2]))
#print("can_", can_)
res = []
if N in can_:
    for i in can_:
        if i==N:
            res.append(can_.index(i))
    #print("res", res)

    print(prod_to_num[min(res)])
else: print(0)

# Discussion
"""

"""