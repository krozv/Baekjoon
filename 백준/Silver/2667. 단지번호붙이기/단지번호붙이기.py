# 2667. 단지번호붙이기
"""
1 집 있음, 0 집 없음
델타 사용해서 구역 구획
오름차순으로 빼
"""
def dfs(x, y):
    q = deque()
    q.append([x, y])
    arr[x][y] = 0
    apt = 1
    while q:
        for d in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            ni = q[0][0] + d[0]
            nj = q[0][1] + d[1]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1:
                arr[ni][nj] = 0
                apt += 1
                q.append([ni, nj])
        q.popleft()
    return apt

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().strip('\n'))) for _ in range(N)]
# v = [[0] * N for _ in range(N)]

cpx = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            cpx.append(dfs(i, j))
cpx.sort()
print(len(cpx))
for apt in cpx:
    print(apt)