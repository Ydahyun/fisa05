# <문제> 왕실의나이트: 문제 설명
"""
8*8 나이트 가능한 수

"""

# 입력
"""
'al'
"""

# 출력
"""
2
"""

# 내 풀이 아이디어
"""

"""

#input_data = input()
input_data = 'al'
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) +1

steps=[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

result = 0
for step in steps:
    next_row = row+step[0]
    next_column = column + step[0]
    
    if next_row >=1 and next_row <=8 and next_row >=1 and next_column <=8:
        result +=1

print(result)




# 동빈나 풀이



# Discussion
"""

"""