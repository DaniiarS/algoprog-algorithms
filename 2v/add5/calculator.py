def calculator(desired_number: int)-> int:
    line = [0, 0, 0]
    line[0] = 0
    line[1] = 1
    line[2] = 1

    if desired_number < 3:
        return line[desired_number-1]

    line = [1 for i in range(desired_number)]
    for i in range(3, desired_number):
        if (i+1) % 3 == 0:
            if (i+1) % 2 == 0:
                line[i] = min(line[i//3], line[i//2], line[i-1]) + 1
            else:
                line[i] = min(line[i//3], line[i-1]) + 1
        elif (i+1) % 2 == 0:
            line[i] = min(line[i//2], line[i-1]) + 1
        else:
            line[i] = line[i-1] + 1

    return line[desired_number-1]

n = int(input())
print(calculator(n))