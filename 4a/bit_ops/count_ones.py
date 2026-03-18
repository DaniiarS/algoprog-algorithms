def main():
    a = int(input())
    count = 0

    while(a):
        if a % 2 == 1:
            count += 1
        a = a >> 1
        
    print(count)

if __name__ == '__main__':
    main()