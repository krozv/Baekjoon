# 10026. 적록색약
"""
RGB그림.. 이거 bfs맞아?
탐색횟수를 숫자로 표현해서, 갈 수 있는 길과 없는 길을 구분
탐색한 숫자를 출력
(예)
적록색약이 아닌 사람의 경우
(0,0)에서 출발해. -> 길이 막힘. +1를 해서 visit 시작
"""
def bfs(arr, coordi):
    q = deque()
    q.append([coordi[0], coordi[1]])
    # 처음 좌표
    v[coordi[0]][coordi[1]] = 1
    while q:
        # 탐지 컬러 정함
        clr = arr[q[0][0]][q[0][1]]
        # 탐지 시작 - 델타 이용
        for d in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            ni = q[0][0] + d[0]
            nj = q[0][1] + d[1]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == clr and v[ni][nj] == 0:
                    q.append([ni, nj])
                    v[ni][nj] = 1
        q.popleft()
    return 1


import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
color = [list(input().strip('\n')) for _ in range(N)]
color_v2 = [[0] * N for _ in range(N)]

v = [[0] * N for _ in range(N)]
area = 0
for i in range(N):
    for j in range(N):
        if v[i][j] == 0:
            bfs(color, [i, j])
            area += 1
print(area, end=' ')

for i in range(N):
    for j in range(N):
        if color[i][j] == 'R':
            color_v2[i][j] = 'G'
        else:
            color_v2[i][j] = color[i][j]

v = [[0] * N for _ in range(N)]
area = 0
for i in range(N):
    for j in range(N):
        if v[i][j] == 0:
            bfs(color_v2, [i, j])
            area += 1
print(area)
