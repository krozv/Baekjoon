# 15904. UCPC는 무엇의 약자일까?
string = list(input())
upper_char = []
UCPC = ['U', 'C', 'P', 'C']
check = False
for index in range(len(UCPC)):
    if UCPC[index] in string:
        string = string[string.index(UCPC[index])+1:]
        if index == 3:
            check = True
    else:
        break

if check:
    print('I love UCPC')
else:
    print('I hate UCPC')