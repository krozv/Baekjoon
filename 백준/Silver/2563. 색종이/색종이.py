# 색종이
import sys
paper = 100 * 100
color_paper = 10 * 10

coordi = [[0 for i in range(100)] for j in range(100)]

num = int(input())
where = []
for i in range(num):
    where.append(list(map(int, sys.stdin.readline().split())))

for i in range(num):
    for k in range(100):
        for l in range(100):
            if where[i][0] <= k < where[i][0]+10 and where[i][1] <= l < where[i][1]+10:
                coordi[k][l] = 1

a = 0
for i in range(100):
    for j in range(100):
        if coordi[i][j] == 1:
            a += 1

print(a)