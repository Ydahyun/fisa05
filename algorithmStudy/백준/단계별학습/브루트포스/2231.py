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

문제에서 216이 주어지면 나는 198을 출력해야함.
198+1+9+8 = 216
가능한 숫자를 [0,1,2,3,4,5,6,7,8,9] 리스트로 만들어서
(['0','1','2','3','4','5','6','7','8','9'] str로 만들어야겠다)
(예를들어 세자리수이면 000~999까지 1000개.)
그러면 첫째 줄에 숫자가 주어지니까 수가 몇자리 수 인지 확인해서 중복 순열돌려야겠네
# 중복순열 코드
from itertools import product
data = ['A', 'B', 'C']
result = list(product(data, repeat=2)) # <- 이자리에 몇자리수인지 들어갈 예정
print(result)

그리고 문자열로도 ['000', '001', ... , '999'] 넣고,
int형으로도 [000, 001, ..., 999] 만들어서 넣자.
인트형은 안해도되나?
일단은.. int형은 보류.
===여기까지 구현완. int형은 보류.

문자열 인덱스로 호출해서 문자열리스트[i] + ...[i][0]+[i][1]+[i][2] 해서
입력값 N과 맞는지 확인. 몇 번째 인덱스(i)인지 꺼내보는것도 좋을 것 같음.
웅 꺼내야겠다. 왜냐면 같은 게 있을 수 있으니까 인덱스꺼내서 따로 리스트에 저장하고,
min()써서 작은거 출력하면 되겠다.
여기서 만약 없으면 0 출력.
"""


#N=input()
N='216' # 문자열로 받을 예정임
N_len=len(N)


from itertools import product
jaeRyo=['0','1','2','3','4','5','6','7','8','9']
result = list(product(jaeRyo, repeat=N_len)) # <- 이자리에 몇자리수인지 들어갈 예정
#print(result, '\n', len(result))

result_int = [int(''.join(t)) for t in result]
#result_int = [int(a)*100 + int(b)*10 + int(c) for (a, b, c) in result]
#print(result_int, '\n', len(result_int))




can_saengSungJa=[]
for i in range(len(result)):
    # 나중에 시간초과걸리면 리스트 컴프레헨션으로 바꾸자
    can_saengSungJa.append(result_int[i] + int(result[i][0]) + int(result[i][1]) + int(result[i][2]))
    #print(f"{result_int[i]} + {int(result[i][0])} + {int(result[i][1])} + {int(result[i][2])}")
#print(f"{result_int[198]} + {int(result[198][0])} + {int(result[198][1])} + {int(result[198][2])}")
#print(result_int[198] + int(result[198][0]) + int(result[198][1]) + int(result[198][2]))
                        #  ~~~~~~~~~~~~~
                        # 여기가 ('0', '0', '0') 튜플 형식이네
                        # 어떻게 해결할까?
                        # 1. 하나씩 붙여서 int로 형변환하기.
                        # 2. 그냥 range()로 만들기..? 이거 근데 잘모르겟다.
                        # 역시 모를땐 무식하게 노가다지 1번으로 가보자잇
                        # 아니다 이거 인트형으로 만들면 된다 위에서 보류했던거 그냥 만들면 된다
#print(can_saengSungJa[198], '\n', len(can_saengSungJa))
# 생성자 가능한 수를 인덱스로 담기

#print(can_saengSungJa[198])
can_saengSungJa_idxLi=[]
for i in range(len(can_saengSungJa)):
    if can_saengSungJa[i] == int(N):
        #can_saengSungJa_idxLi.append(can_saengSungJa.index(can_saengSungJa[i]))
        # 아 근데 위에처럼 하면 같은 숫자가 있어도 첫 번째 값의 인덱스만 가져오잖아..
        # 그냥 i로 넣어주면 되겠네 ㅋ
        can_saengSungJa_idxLi.append(i)  # 요런식으로 하면 i가 인덱스니까 되겠다.
#print(can_saengSungJa_idxLi)
#print(can_saengSungJa_idxLi)


# 자자 마지막이다.
if int(N) in can_saengSungJa:
    print(min(can_saengSungJa_idxLi))
else: print(0)
