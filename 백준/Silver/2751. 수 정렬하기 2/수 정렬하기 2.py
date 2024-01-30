# 2751. 수 정렬하기 2
import sys
N = int(sys.stdin.readline())
num_list = []
positive_count = [0] * 1000001
negative_count = [0] * 1000001
for i in range(N):
    num = int(sys.stdin.readline())
    if num >= 0:
        positive_count[num] = 1
    else:
        negative_count[-num] = 1

for i in range(1000000, 0, -1):
    if negative_count[i] == 1:
        print(-i)
for i in range(1000001):
    if positive_count[i] == 1:
        print(i)

