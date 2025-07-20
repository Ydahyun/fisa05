# 백준 1316번
# <문제> 그룹 단어 체커: 문제 설명
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
N = int(input())
cnt = N

for i in range(N):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break

print(cnt)





# 동빈나 풀이

# Discussion
"""

"""