input_data = []
while True:
    try:
        input_data.append(input())
    except:
        break

print('\n'.join(input_data))