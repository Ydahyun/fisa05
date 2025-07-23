# 백준 10809번
# <문제> 알파벳 찾기: 문제 설명
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
dict_cnt = {}
s=input()
for i in range(ord('a'), ord('z')+1):
    dict_cnt[chr(i)]=-1


for i, k in enumerate(s):
    if dict_cnt[k] != -1:
        continue
    else: dict_cnt[k] = i
print(*dict_cnt.values())
# Discussion
"""

"""