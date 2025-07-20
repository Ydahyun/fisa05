# 재귀함수
# 스택 라이브러리 대신에 재귀함수 이용하는 경우가 많다

# 팩토리얼 함수 구현

def factorial(n):
    sum=1
    if n == 1:
        return 1
    sum *= n
    return sum * factorial(n-1)

n=5

res = factorial(n)

print(res)