import sys
input = sys.stdin.readline
N = int(input())
memo = [0] * (N + 1)
if N >= 1:
    memo[1] = 1
if N >= 2:
    memo[2] = 2
for i in range(3, N+1):
    memo[i] = (memo[i-1] + memo[i-2]) % 15746
print(memo[N])