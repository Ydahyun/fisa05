# 백준 2839번
# <문제> 설탕 배달: 문제 설명
"""

"""

#N = int(input())
N=11
cnt=0

def checker(N, cnt):
    cnt_3=0
    cnt_5=0
    
    if (N%5) % 3 ==0:
        cnt = (cnt_5:=N//5) + (cnt_3:=(N%5)//3)
    else: cnt = (cnt_3:=N//3) + (cnt_5:=(N%3)//5)
    print(cnt)


# 정확히 못만드는거
if (N%5) % 3 ==0:
    checker(N,cnt)
    #exit()
elif (N%3) % 5 ==0:
    checker(N,cnt)
    #exit()
elif (N%5) % 3 !=0:
    print(-1)
    #exit()
elif (N%3) % 5 !=0:
    print(-1)

