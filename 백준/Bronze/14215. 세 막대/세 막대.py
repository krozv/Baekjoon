sticks = list(map(int, input().split()))
max_stick = max(sticks)
sticks.pop(sticks.index(max_stick))
if max_stick >= sum(sticks):
    difference = max_stick - sum(sticks)
    max_stick -= difference+1
print(max_stick+sum(sticks))