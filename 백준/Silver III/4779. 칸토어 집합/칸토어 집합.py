# 4779 칸토어 집합
"""
-가 3^N개 있는 문자열
문자열을 3등분 -> 가운데를 공백으로 전환
모든 선의 길이가 1이면 멈춤
결과 출력하는 프로그램
"""
def f(string, N):
    if N == 1:
        return string
    str1 = string[:N//3]
    str2 = string[N//3:2*N//3]
    str3 = string[N//3:2*N//3]
    str1 = f(str1, N//3)
    str2 = str2.replace('-', ' ')
    str3 = f(str3, N//3)
    return str1+str2+str3


import sys
input = sys.stdin.readline
num_list = []
while True:
    try:
        num_list.append(int(input()))
    except:
        break
for N in num_list:
    string = '-' * (3**N)
    f(string, 3**N)
    print(f(string, 3**N))
'''
-
- -
- -   - -         - -   - -
- -   - -         - -   - -
- -   - -
- -   - -
'''