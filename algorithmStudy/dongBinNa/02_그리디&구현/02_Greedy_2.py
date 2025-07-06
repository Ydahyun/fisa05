# <문제> 곱하기 혹은 더하기: 문제 설명
"""
각 자리가 숫자(0부터 9)로만 이루어진 문자열 S가 주어졌을 때, 
왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 
숫자 사이에 X 혹은 + 연산자를 넣어 결과적으로
만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요.
단, +보다 X를 먼저 계산하는 일반적인 방식과는 달리,
모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정합니다.

예를들어 02984라는 문자열로 만들 수 있는 가장 큰 수는
((((0+2)*9)*9)*4)=576입니다.
또한 만들어질 수 있는 가장 큰 수는 항상 20억 이하의 정수가 되도록
입력이 주어집니다.
"""

# 내 풀이
"""
내 풀이 아이디어
일단은 왼쪽에서부터 값 확인해서 0이면 더하기 넣어주고,
아니면 곱하기 넣어주면 되겠네.
"""
S = "02984"
#S = "120"

res = 0

for i in S:
    if int(i)==0 or res==0:
        res += int(i)
    else: 
        res *= int(i)

print("res",res)
        

# 동빈나 풀이

#data = input()
#result = int(data[0])
data = ['02984']
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 0 혹은 1 인경우
    # 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print("dongBinNa", result)  # 왜 결과다르냐..? 동빈나 틀림?


print("Discussion")
print("그러네 1곱하면 의미 없으니까 1을 더해주는게 낫네 이거 생각못했다.")

# 다시 내 코드 수정

S = "01184"
#S = "120"

res = 0

for i in S:
    if int(i)==0 or res==0 or int(i)==1:
        res += int(i)
    else: 
        res *= int(i)

print("res",res)