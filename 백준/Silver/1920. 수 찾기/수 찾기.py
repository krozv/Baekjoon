# 1920 수 찾기
'''
N개의 정수 A[1] ~ A[N] 이 주어졌을 때 X 정수 찾기
N 자연수 1 <= N <= 100,000
n_list N개의 자연수 array
M 수 1 <= M <= 100,000
m_list M개의 수들 array
m_list의 수들이 n_list안에 존재하는 지 확인
-2^31 <= A < 2^31
'''
import sys
input = sys.stdin.readline

N = int(input())
n_list = list(map(int, input().split()))
M = int(input())
m_list = list(map(int, input().split()))

# n_list를 정렬 -> 선택 정렬
n_list.sort()

# m_list에서 num를 하나씩 꺼낸 후 이진탐색
for i in range(M):
    start = 0
    end = N - 1
    while start <= end:
        middle = (start+end)//2
        if n_list[middle] == m_list[i]:
            # print(m_list[i])
            m_list[i] = 1
            break
        elif n_list[middle] < m_list[i]:
            start = middle + 1
        else:
            end = middle - 1
    if start > end:
        m_list[i] = 0

for i in range(M):
    print(m_list[i])