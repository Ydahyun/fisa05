# <문제> 시각: 문제 설명
"""
정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서
3이 하나라도 포함되는 모든 경우의 수를 구하는 프로글매을 작성하세요.
예를들어 1을 입력했을때 다음은 3이 하나라도 포함되어 있으므로 세어야하는 시각입니다.
-00시00분3초
-00시13분30초
반면에 다음은 3이 하나도 포함되어 있지 않으므로 세면 안되는 시각입니다.
--00시02분55초
--01시27분45초

"""

# 입력
"""
0<=N<=23
5
"""

# 출력
"""
11475 시간제한 2초
"""

# 내 풀이 아이디어
"""
리스트 원소 3개로해서 해볼까
[0,0,0] ~ [23,59,59]

"""

#N=int(input())
N=5
time_list = [0,0,0]
cnt = 0

while True:
    if time_list[2] != 60:  # 초
        time_list[2] +=1
        if time_list[-1] == 3 or time_list[-1] == 13 or time_list[-1] == 23 or time_list[-1] == 33 or time_list[-1] == 43 or time_list[-1] == 53 or time_list[-1] == 30 or time_list[-1] == 31 or time_list[-1] == 32 or time_list[-1] == 34 or time_list[-1] == 35 or time_list[-1] == 36 or time_list[-1] == 37 or time_list[-1] == 38 or time_list[-1] == 39:
            cnt +=1
    else:
        time_list[2] =0     # 분
        if time_list[1] !=60:
            time_list[1] +=1
            if time_list[1] == 3 or time_list[1] == 13 or time_list[1] == 23 or time_list[1] == 33 or time_list[1] == 43 or time_list[1] == 53 or time_list[1] == 30 or time_list[1] == 31 or time_list[1] == 32 or time_list[1] == 34 or time_list[1] == 35 or time_list[1] == 36 or time_list[1] == 37 or time_list[1] == 38 or time_list[1] == 39:
                cnt +=1
        else:               # 시
            time_list[1] =0
            time_list[0] +=1
            
            if time_list[0] == 3 or time_list[0] == 13 or time_list[0]==23:
                cnt+=1
    
    if time_list[0] == N and time_list[1]==59 and time_list[2]==59:
        break


print(cnt)




# 동빈나 풀이


h=5
count=0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j)+str(k):
                count+=1
    
print(count)

# Discussion
"""

"""