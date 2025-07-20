# 백준 25206번
# <문제> 너의평점은: 문제 설명
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

sc = {"A+":4.5,"A0":4.0,"B+":3.5,"B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0.0}
res=0
total_s1=0
try:
    while True:


        s = input().split()
        if s[2] == "P":
            continue
        res += float(s[1])*sc[s[2]]
        total_s1 += float(s[1])
except EOFError:
    pass

fin_res = res/total_s1
print(fin_res)

# 동빈나 풀이

# Discussion
"""

"""