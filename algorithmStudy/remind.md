###### 순열
```python
from itertools import permutations

data = ['A', 'B', 'C']

result = list(permutations(data, 3))
print(result)

# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
```
###### 조합
```python
from itertools import combinations

data = ['A', 'B', 'C']

result = list(combinations(data, 2))
print(result)

# [('A', 'B'), ('A', 'C'), ('B', 'C')]
```
###### 중복 순열
```python
from itertools import product

data = ['A', 'B', 'C']

result = list(product(data, repeat=2))
print(result)

# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
```
###### 중복 조합
```python
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']

result = list(combinations_with_replacement(data, 2))
print(result)

# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
```
###### Counter - 등장 횟수 세능 기능을 제공
```python
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))

# 3
# 1
# {'red': 2, 'blue': 3, 'green': 1}
```
###### 최대공약수(GCD)와 최소공배수(LCM)
```python
import math

# 최소 공배수(LCM)를 구하는 함수
def lcm(a,b):
    return a*b // math.gcd(a,b)

a=21
b=14

print(math.gcd(21,14))  # 7
print(lcm(21,14))       # 42
```