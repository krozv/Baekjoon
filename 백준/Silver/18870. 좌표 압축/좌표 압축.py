# 18870 좌표 압축
'''
N개의 좌표 x
순서를 표기한 리스트 생성 후 출력
'''
import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
new_list = list(set(num_list))
idx_list = list(range(len(num_list)))
new_list.sort()

num_dict = dict(zip(new_list, idx_list))
# print(num_dict)

for i in range(N):
    num_list[i] = num_dict[num_list[i]]
print(*num_list)