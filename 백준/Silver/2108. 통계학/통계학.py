# 2108 통계학
import decimal
import sys
input = sys.stdin.readline
N = int(input())
num_list = [int(input()) for _ in range(N)]
# counting sort
# counting sort를 위해 num_list 내 숫자와 동일한 인덱스의 값을 1씩 증가
count = [0] * 8001
total = 0   # 총합을 구하기 위한 변수 total
max_cnt = 0
for i in range(N):
    count[num_list[i]+4000] += 1
    total += num_list[i]
    if max_cnt < count[num_list[i]+4000]:
        max_cnt = count[num_list[i]+4000]

frq = 0
frq_num = 0

# count의 누적합을 구함
for i in range(8001):
    if count[i] == max_cnt and frq < 2:
        # print('test', count[i])
        frq_num = i-4000
        frq += 1
    if i > 0:
        count[i] += count[i-1]

# 누적합을 기준으로 정렬
sorted_num_list = [0] * N
for num in num_list:
    if count[num+4000] != 0:
        sorted_num_list[count[num+4000]-1] = num
        count[num+4000] -= 1

max_num = sorted_num_list[-1]   # 최댓값
min_num = sorted_num_list[0]    # 최솟값

print(round(total/N))           # 산술평균
print(sorted_num_list[N//2])    # 중앙값
print(frq_num)                  # 최빈값
print(max_num - min_num)        # 범위