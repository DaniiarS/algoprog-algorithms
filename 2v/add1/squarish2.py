def max(a: int, b:int)-> int:
    if a > b:
        return a
    
    return b

def min(a:int, b:int)-> int:
    if a < b:
        return a

    return b

def count_consecutive_horizontal(line, col):
    size = len(line)
    count = 0

    while col < size:
        if line[col] == "#":
            count += 1
        else:
            break
        
        col += 1
    
    return count

def count_consecutive_vertical(square, row, col):
    size = len(square)
    count = 0

    while row < size:
        if square[row][col] == "#":
            count += 1
        else:
            break
        row += 1
    
    return count

def find_maximum_square(square:list)->int:
    size = len(square)
    max_square = 0
    for i in range(size):
        for j in range(size):
            if square[i][j] == "#":
                side_a = count_consecutive_horizontal(square[i], j)
                side_b = count_consecutive_vertical(square, i, j)
                
                current_square = max(side_a, side_b) - min(side_a, side_b)
                if current_square > max_square:
                    max_square = current_square
    
    return max_square

n = int(input())
square = []

for i in range(n):
    line = list(input())
    square.append(line)

print(find_maximum_square(square))