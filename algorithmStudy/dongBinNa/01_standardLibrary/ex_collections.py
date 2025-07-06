###### Counter - 등장 횟수 세능 기능을 제공
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))

# 3
# 1
# {'red': 2, 'blue': 3, 'green': 1}