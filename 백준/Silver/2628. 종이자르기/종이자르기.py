width, length = map(int, input().split())
N = int(input())
# 0은 가로, 1은 세로
# 그 다음 숫자는 자르는 번호
paper = []
area = width * length
paper_width = list(range(width))
paper_length = list(range(length))

col = []
row = []
for _ in range(N):
    a, b = map(int, input().split())
    if a == 0:
        col.append(b)
    elif a == 1:
        row.append(b)
row.sort()
col.sort()

def list_slice(paper, cut):
    cut_col = []
    if len(cut) == 0:
        cut_col.append(paper)
    for i in range(len(cut)):
        if len(cut) == 1:
            cut_col.append(paper[:(cut[i])])
            cut_col.append(paper[cut[i]:])
        elif i == 0:
            cut_col.append(paper[:(cut[i])])
        elif i == len(cut) - 1:
            cut_col.append(paper[(cut[i - 1]):(cut[i])])
            cut_col.append(paper[cut[i]:])
        else:
            cut_col.append(paper[(cut[i - 1]):(cut[i])])
    return cut_col


cut_row = list_slice(paper_width, row)
cut_col = list_slice(paper_length, col)

list_len = []
for i in range(len(cut_row)):
    list_len.append(len(cut_row[i]))
max_row = max(list_len)

list_len = []
for j in range(len(cut_col)):
    list_len.append(len(cut_col[j]))
max_col = max(list_len)

print(max_col * max_row)