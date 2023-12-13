alp = []
word = []

# alphabet 모음 만듦
for i in range(ord('A'),ord('Z')+1):
    alp.append(chr(i))

# 다이얼 숫자에 따른 알파벳 할당
alp.remove('S')
alp.remove('Z')
for j in range(0, len(alp), 3):
    word.append(''.join(alp[j:j+3]))
word[5] = word[5] + 'S'
word[7] = word[7] + 'Z'

case = list(input())
time = []

# print(word)
# input에 대응하는 다이얼 숫자 찾음
for k in range(len(case)):
    for l in range(len(word)):
        if case[k] in word[l]:
            time.append(l+2)

# 다이얼 숫자에 따른 최소 시간 계산
for i in range(len(time)):
    min_time = sum(time) + len(time)

print(min_time)