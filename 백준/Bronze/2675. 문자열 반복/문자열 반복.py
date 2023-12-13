# 문자열 반복
T = int(input())
case = []
output = []

# 입력된 문자열 list에 저장
for i in range(T):
    case.append(input())

# list 분리 및 분리된 조건에 따른 문자열 반복 -> 출력
for i in range(T):
    rep, test = case[i].split()
    rep = int(rep)
    test = list(test)
    for j in range(len(test)):
        output.append(test[j] * rep)
        # print(output)
    print(''.join(output))
    output = []