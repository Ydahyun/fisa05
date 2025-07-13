import sys
import heapq

def heapsort(iterable):
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)  # 맥스힙만드려면 -value
    print("완전이진트리순서대로 민힙구성", h)  # min-heap 완전이진트리순서대로 구성됨을 확인할 수 있음

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))  # 여기도 맥스힙만들때 부호복원

    return result

n = 5
arr = [5,4,10,2,1]
res = heapsort(arr)

for i in range(n):
    print(res[i])
    
print(res)
