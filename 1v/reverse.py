def reverse(line: str) -> str:
    reversed_line = list(line)
    start, end = 0, len(line) - 1

    while(start <= end):
        reversed_line[start], reversed_line[end] = reversed_line[end], reversed_line[start]
        start += 1
        end -= 1
    
    return ''.join(reversed_line)

line = input()
print(reverse(line))