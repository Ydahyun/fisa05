# 백준 2231번
# <문제> 영화감독 슘: 문제 설명
"""

"""

N = int(input())
#N=2
cnt=0
num=666

while True:  # 계속 반복하다가 666나오는것만 카운트
    if '666' in str(num):
        cnt +=1
        if cnt == N:  # N이 나오면 반복멈춰
            break
    num +=1

print(num)