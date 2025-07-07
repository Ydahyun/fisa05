# 디버깅 해보기
data = ['02984']
#data = '02984'

result = int(data[0][0])
print(data[0][0], "a")
print(data[0][1], "b")
print(data[0][2], 'c')
print(data[0][3], 'd')
print(data[0][4], 'e')

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 0 혹은 1 인경우
    # 곱하기보다는 더하기 수행
    num = int(data[0][i])
    if num <= 1 or result <= 1:
        result += num
        print(num, 'f')
    else:
        result *= num
        print(num, 'g')

print("dongBinNa", result)  # 왜 결과다르냐..? 동빈나 틀림?