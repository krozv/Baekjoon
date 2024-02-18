# 1012. 유기농 배추 - BFS
"""
BFS 이용하면 금방 풀리겠넹
"""
def bfs(x, y):
    q = collections.deque()
    q.append([x, y])
    cabbage[x][y] = 0
    global cnt
    cnt += 1
    while q:
        for d in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            ni = q[0][0] + d[0]
            nj = q[0][1] + d[1]
            if 0<=ni<N and 0<=nj<M and cabbage[ni][nj] == 1:
                q.append([ni, nj])
                cabbage[ni][nj] = 0
                cnt += 1
        q.popleft()


import collections
import sys
input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    M, N, K = map(int, input().split()) # 가로, 세로, 위치
    cabbage = [[0] * M for _ in range(N)]
    for _ in range(K):
        i, j = map(int, input().split())
        cabbage[j][i] = 1
    cnt = 0
    worm = 0
    while cnt < K:
        for i in range(N):
            for j in range(M):
                if cabbage[i][j] == 1:
                    bfs(i, j)
                    worm += 1
    print(worm)
