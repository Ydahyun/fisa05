import sys
import heapq

def heapsort(iterable):
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))

    return result

n = 10
arr = [9,5,2,1,7,65,2,1,8,2]
res = heapsort(arr)

for i in range(n):
    print(res[i])
    
print(res)
