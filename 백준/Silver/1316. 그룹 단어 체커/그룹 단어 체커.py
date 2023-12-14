# input을 분할된 리스트로 받음
N = int(input())
a = 0
seq = 0
not_group = []
for i in range(N):
    word = list(input())

    # 사용된 알파벳 추출
    used_alpha = list(set(word))
    used_alpha.sort()

    # 해당 알파벳의 사용횟수(count) 추출
    for j in range(len(used_alpha)):
        first = word.index(used_alpha[j])
        count = word.count(used_alpha[j])
        # print(used_alpha[j], first, count)

        if count > 1:
            for k in range(first, first + count):
                if used_alpha[j] != word[k]:
                    not_group.append(''.join(word))
                    break

print(N - len(set(not_group)))