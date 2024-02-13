# 1874. 스택 수열

n = int(input())
seq = [int(input()) for _ in range(n)]   # 수열 sequence
num_list = list(range(n, 0, -1))

stack = []
output = []
new_seq = []
while seq:
    if not stack:
        if not num_list:
            output = None
            break
        num = num_list.pop()
        stack.append(num)
        output.append('+')
    # stack에 요소 존재
    else:
        # stack안에 수열 존재
        # print(seq[0])
        if seq[0] in stack:
            while stack[-1] != seq[0]:
                elem = stack.pop()
                output.append('-')
            # stack[top] == seq[idx] 이므로
            stack.pop()
            output.append('-')
            seq.pop(0)
        elif seq[0] in num_list:
            while stack[-1] != seq[0]:
                num = num_list.pop()
                stack.append(num)
                output.append('+')
            # stack[top] == seq[idx] 이므로
            stack.pop()
            output.append('-')
            seq.pop(0)
        else:
            output = None
            break
    # print(stack)
if output:
    for elem in output:
        print(elem)
else:
    print('NO')