# 바이러스
"""
visit 수 입력
"""


def bfs(start):
    q = deque()
    q.append(start)
    v[start] = 1
    computer = 0
    while q:
        for i in adj[q[0]]:
            if not v[i]:
                v[i] = 1
                q.append(i)
                computer += 1
        q.popleft()
    return computer


import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    adj[n1].append(n2)
    adj[n2].append(n1)
v = [0] * (N+1)
print(bfs(1))