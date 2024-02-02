# 18870 좌표 압축
'''
N개의 좌표 x
순서를 표기한 리스트 생성 후 출력
'''
import sys
input = sys.stdin.readline

N = int(input())
# 입력받은 num_list 생성
num_list = list(map(int, input().split()))
# 집합으로 변환하여 중복된 숫자 제거 및 정렬
new_list = list(set(num_list))
new_list.sort()
# 정렬된 리스트의 인덱스 리스트 생성
idx_list = list(range(len(new_list)))
# 정렬된 new_list를 key로, idx_list를 value로 하는 dict 생성
num_dict = dict(zip(new_list, idx_list))
# dict의 키에 일치하는 value로 num_list 변환
for i in range(N):
    num_list[i] = num_dict[num_list[i]]
print(*num_list)