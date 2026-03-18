def main():
    s = input()
    line = 0
    
    for ch in s:
        x = 1
        x = x << (ord(ch) - ord('a'))

        if (x & line) > 0:
            print(ch)
            break
        
        line = line | x



if __name__ == '__main__':
    main()


# AND - Masking
# OR - Mergning

# XOR properties:
# x ^ x = 0
# x ^ 0 = x