# 27497. 알파벳 블록
"""
기능
1. 문자열 맨 뒤에 블록 추가
2. 문자열 맨 앞에 블록 추가
3. 문자열을 구성하는 블록 중 가장 나중에 추가된 블록 제거
N: 버튼을 누른 횟수
"""
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
button_list = [input() for _ in range(N)]
deq = deque()
stk = []
for button in button_list:
    if button[0] != '3':
        button, char = button.split()
        if button == '1':
            deq.append(char)
            stk.append(1)
        else:
            deq.appendleft(char)
            stk.append(2)
    else:
        if stk:
            if stk[-1] == 1:
                deq.pop()
            else:
                deq.popleft()
            stk.pop()
if deq:
    print(''.join(deq))
else:
    print(0)
