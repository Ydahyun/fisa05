# 백준 3003번
# <문제> 킹, 퀸, 룩, 비숍, 나이트, 폰: 문제 설명
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
def check(dh_find):
    
    correct_li=[1,1,2,2,2,8]
    print_li=[0,0,0,0,0,0]  
        
    for i in range(len(correct_li)):
        if dh_find[i] > correct_li[i]:
            print_li[i] = correct_li[i] - dh_find[i]
        elif dh_find[i] == correct_li[i]:
            print_li[i] = 0
        else:
            print_li[i] = correct_li[i] - dh_find[i]
    return print_li
#dh_find = int(input().split())
dh_find = [0,1,2,2,2,7]

res= check(dh_find)
print(res)


# Discussion
"""

"""