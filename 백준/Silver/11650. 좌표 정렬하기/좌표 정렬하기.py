# 11650 좌표 정렬하기
'''
N: 점의 개수
xi, yi = ( , )
x좌표 같으면 y좌표 순으로
'''
N = int(input())
num_list = []
for _ in range(N):
    num_list.append(list(map(int, input().split())))
num_list.sort(key=lambda x: (x[0], x[1]))
for num in num_list:
    print(*num)