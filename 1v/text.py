def is_symbol(char:chr) -> bool:
    capitalChar = ( ord(char) >= ord('A') and ord(char) <= ord('Z') )
    lowerChar = ( ord(char) >= ord('a') and ord(char) <= ord('z') )

    if capitalChar or lowerChar:
        return False

    return True

def reverse_substring(line:list, left:int, right:int) -> list:
    while(left < right):
        line[left], line[right] = line[right], line[left]

        left += 1
        right -= 1

def reverse(line: list) -> list:

    size = len(line)
    start, end = 0, 0

    modified = False
    no_symbol = True

    for i in range(size):
        if is_symbol(line[i]):
            no_symbol = False
            
            if modified:
                continue
            
            end = i - 1
            reverse_substring(line, start, end)
            modified = True
        else:
            # first char of the new substring 
            if modified:
                start = i
                modified = False
    
    if no_symbol:
        reverse_substring(line, 0, size-1)

    return ''.join(line)



result = []
with open("input.txt", "r") as file:
    lines = file.readlines()    
    for line in lines:
        result.append(reverse(list(line)))

for line in result:
    print(line, end="")
