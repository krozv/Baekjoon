'''
(와 )로만 구성
기본 VPS (), (X), (())(), ((())),

'''


def confirm_data(data):
    for i in range(len(data)-1):
        if '(' in data[i]:
            if ')' in data[i + 1]:
                remove_index = i
                data.pop(remove_index)
                data.pop(remove_index)
                break
    return data


import sys
T = int(input())
for _ in range(T):
    data = sys.stdin.readline().strip('\n')
    i = 0
    while True:
        if data == '':
            print('YES')
            break
        elif '()' not in data:
            print('NO')
            break
        else:
            start_index = data.index('()')
            data = data[:start_index] + data[start_index+2:]

