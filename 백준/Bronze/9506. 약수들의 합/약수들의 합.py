input_data = True
factor = []
while input_data:
    a = int(input())
    i = 0
    output = f"{a} ="
    if a == -1:
        break
    else:
        for i in range(a-1):
            i += 1
            if a % i == 0:
                factor.append(i)
                output = output + f" {factor[-1]} +"
        if a == sum(factor):
            print(output[0:-2])
        else:
            print(f"{a} is NOT perfect.")
        factor = []