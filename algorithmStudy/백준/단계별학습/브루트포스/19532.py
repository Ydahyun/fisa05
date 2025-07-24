# 백준 19532번
# <문제> 수학은 비대면강의입니다: 문제 설명
"""
x  + 3y = -1
4x +  y =  7

위의 열에 4를 곱해, 아래 열에 1을 곱해.
a,b,c에 d를 곱하고, d,e,f에 a를 곱하는거지.

4x + 12y = -4
4x + y    = 7

그리고 빼,
11y = -11

x는 어차피 소거되니까 곱해진b와 곱해진 e를 서로 빼주고,
곱해진 c와 곱해진f를 서로 빼줘

이거를 차례로,
h 라하고 i라 해.

i를 h로 나누면 끝~
사실상 행렬로 푸는거지
"""

a,b,c,d,e,f = map(int, input().split())
#print(a,b,c,d,e,f)
ad=a*d
bd=b*d
cd=c*d
da=d*a
ea=e*a
fa=f*a
#print(ad,bd,cd,da,ea,fa)
h=bd-ea
i=cd-fa
if h==0.0:
    y=i
else:
    y=i/h

if a==0.0 and d!=0.0:
    x = (f - e * y)/d
elif a!=0.0 and d==0.0:
    x = (c - b * y)/a
else:
    x = (c - b * y) / a

print(int(x), int(y))

# 두번째 식을 고려안했네 d=0일때만 고려했어 a=0인 경우도 있잖아.