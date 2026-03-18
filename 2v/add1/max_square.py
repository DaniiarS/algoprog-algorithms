def max_square(n: int):
    square = []
    for i in range(n):
        line = list(input())
        square.append(line)
    
    for line in square:
        print(line)

n = int(input())
max_square(n)