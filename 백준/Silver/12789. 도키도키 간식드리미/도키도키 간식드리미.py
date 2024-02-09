N = int(input())
num_list = list(map(int, input().split()))
stack = []
leave = 1
top = -1

for num in num_list:
    if len(stack):
        while stack[top] == leave:
            leave += 1
            stack.pop()
            top -= 1
            if not len(stack):
                break
    # 대기순서와 번호표가 일치
    if leave == num:
        leave += 1
    else:
    # stack안에 들어갈 번호표
        stack.append(num)
        top += 1
if len(stack):
    for _ in range(len(stack)):
        if stack[top] == leave:
            leave += 1
            stack.pop()
            top -= 1
    else:
        if len(stack):
            print("Sad")
        else:
            print("Nice")
else:
    print("Nice")