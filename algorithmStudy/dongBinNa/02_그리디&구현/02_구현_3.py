# <문제> 왕실의나이트: 문제 설명
"""
알파벳대문자와 숫자(0~9)로만 구성된 문자열이 입력으로주어짐
모든 알파벳을 오름차순으로 정렬하고 이어서 출력한뒤
모든 숫자를 더한 값을 이어서 출력

"""

# 입력
"""
K1KA5CB7
"""

# 출력
"""
ABCKK13
"""

# 내 풀이 아이디어
"""
리스트에 정렬..
영어는 영어끼리 숫자는 숫자끼리
"""
str1 = 'K1KA5CB7'
alphabet_list=[]
val=0
for i in range(len(str1)):
    if str1[i].isalpha():
        alphabet_list.append(str1[i])
    else:
        val += int(str1[i])

alphabet_list.sort()

#print(alphabet_list, val)
# 동빈나 풀이

if val!=0:
    alphabet_list.append(str(val))

print(''.join(alphabet_list))


# Discussion
"""

"""