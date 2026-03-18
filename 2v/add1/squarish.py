def is_edge(i:int, j:int)->bool:
    if i == 0 or j == 0:
        return True
    return False

def min(a:int, b:int)->int:
    if a < b:
        return a
    return b

def find_minimum_square(n:int)->int:
    size = n
    max_square = 0
    
    line = list(input())
    prev_line = [0 if value == "." else 1 for value in line]
    for i in range(1, size):
        line = list(input())
        current_line = [0 for i in range(size)]

        for j in range(size):
            if line[j] == "#":
                if is_edge(i, j):
                    current_line[j] = 1
                else:
                    current_line[j] = min(prev_line[j], current_line[j-1]) + 1
                    if current_line[j] > max_square:
                        max_square = current_line[j]

        prev_line = current_line
    return max_square

n = int(input())

print(find_minimum_square(n))