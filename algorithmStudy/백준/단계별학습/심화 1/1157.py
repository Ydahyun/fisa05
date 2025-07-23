# 백준 1157번
# <문제> 단어공부: 문제 설명
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

word_dict={}

s= input()

for i in s.upper():
    if i in word_dict.keys():
        word_dict[i] +=1
    else:
        word_dict[i] = 1

max_val = max(word_dict.values())
max_keys = [k for k, v in word_dict.items() if v == max_val]

if len(max_keys) > 1:
    print('?')
else:
    print(max_keys[0].upper())

# Discussion
"""

"""