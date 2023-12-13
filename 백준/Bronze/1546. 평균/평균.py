# 평균
N = int(input())
score = list(map(int, input().split()))
Max = max(score)

for i in range(N):
    score[i] = int(score[i]) / Max * 100

print(sum(score)/len(score))