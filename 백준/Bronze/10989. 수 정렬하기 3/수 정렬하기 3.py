# 수 정렬하기 3
'''
N개의 수
1 <= N <= 10,000,000
1 <= 수 <= 10,000
오름차순 정렬
'''
import sys
N = int(sys.stdin.readline())
count = [0] * 10001
num_list = []

for _ in range(N):
    num = int(sys.stdin.readline())
    count[num] += 1

for i in range(1, 10001):
    while True:
        if count[i] == 0:
            break
        else: 
            print(i)
            count[i] -= 1
