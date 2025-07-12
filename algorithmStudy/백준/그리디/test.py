
n, k = 5, 3
list_score = [3,-5,2,-1,4]

# 교실 초기 값 세팅
cnt = 0  # 교실 방문횟수
class_info = []  # 교실의 가중치(int)와 방문횟수(int), 학생들의 목적지(bool)로 2차원 리스트로 넣어줄거임
for score in list_score:
    class_info.append([score, cnt, False])

                     # [[교실가중치, 방문횟수, 학생들의 목적지]]
# print(class_info)  # [[3, 0, False], [-5, 0, False], [2, 0, False], [-1, 0, False], [4, 0, False]]

class_info = [[3, 0, False], [-5, 0, False], [2, 0, False], [-1, 0, False], [4, 0, False]]
for i, val in enumerate(class_info):
    print(val[0], class_info[i+1][0])