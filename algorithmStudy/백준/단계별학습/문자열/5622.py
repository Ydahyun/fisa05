# 백준 5622번
# <문제> 다이얼: 문제 설명
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

"""
#S=input()
S='WA'

time_dict = {}

cnt=0
time=2
for i in range(ord('A'), ord('Z')+1):
    if cnt%3==0:
        time +=1
        time_dict[f'{chr(i)}'] = time
        cnt +=1
    else: 
        time_dict[f'{chr(i)}'] = time
        cnt +=1
time_dict['S'] = 8
time_dict['T'] = 9
time_dict['U'] = 9
time_dict['V'] = 9
time_dict['X'] = 10
time_dict['Y'] = 10
time_dict['Z'] = 10

res=0
#print(time_dict)
for i in S:
    res +=time_dict[i]
    #print(time_dict[i], res)
print(res)

# Discussion
"""

"""